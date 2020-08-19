from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category


class CategoryList(LoginRequiredMixin, ListView):
    model = Category

    def get_queryset(self):
        queryset = Category.objects.all()
        search = self.request.GET.get('search', False)
        if search:
            queryset = queryset.filter(name__contains=search)
        return queryset


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories:list')

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories:list')

class CategoryDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        category = get_object_or_404(Category, pk=pk)
        category.delete()
        return redirect(reverse_lazy('categories:list'))

