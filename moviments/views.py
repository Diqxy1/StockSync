from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy


from .models import ProductStockMoviment
from stock.models import ProductStock


class StockExitMovement(LoginRequiredMixin, ListView):
    model = ProductStockMoviment
    template_name = 'moviments/moviment_list.html'


class StockEntryMoviment(LoginRequiredMixin, ListView):
    template_name = 'moviments/entry_moviment_list.html'
    model = ProductStock

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stocks'] = ProductStock.objects.all()
        #context['moviments'] = ProductStockMoviment.objects.all()
        return context
