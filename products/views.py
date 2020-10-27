from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Product
from .forms import ProductForm


class ProductList(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        queryset = Product.objects.all()
        search = self.request.GET.get('search', False)
        if search:
            queryset = queryset.filter(name__contains=search)
        return queryset


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')


class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:list')


class ProductDelete(LoginRequiredMixin, View):
    def get(self, request, pk):
        product =  get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect(reverse_lazy('products:list'))
