from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Brand


class BrandList(LoginRequiredMixin, ListView):
    model = Brand

    def get_queryset(self):
        queryset = Brand.objects.all()
        search = self.request.GET.get('search', False)
        if search:
            queryset = queryset.filter(name__contains=search)
        return queryset


class BrandCreate(LoginRequiredMixin, CreateView):
    model = Brand
    fields = ['name']
    success_url = reverse_lazy('brands:list')

class BrandUpdate(LoginRequiredMixin, UpdateView):
    model = Brand
    fields = ['name']
    success_url = reverse_lazy('brands:list')

class BrandDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        brand = get_object_or_404(Brand, pk=pk)
        brand.delete()
        return redirect(reverse_lazy('brands:list'))

