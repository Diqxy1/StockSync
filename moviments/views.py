from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy


from .models import ProductStockMoviment
from stock.models import ProductStock


class StockExitMovement(LoginRequiredMixin, ListView):
    model = ProductStockMoviment
    template_name = 'moviments/moviment_list.html'

    def get_queryset(self):
        queryset = ProductStockMoviment.objects.all()
        search = self.request.GET.get('search', False)
        if search:
            queryset = queryset.filter(product_stock__product__name__contains=search)
        return queryset


class StockEntryMoviment(LoginRequiredMixin, ListView):
    template_name = 'moviments/entry_moviment_list.html'
    model = ProductStock

    def get_queryset(self):
        queryset = ProductStock.objects.all()
        search = self.request.GET.get('search', False)
        if search:
            queryset = queryset.filter(product__name__contains=search)
        return queryset
