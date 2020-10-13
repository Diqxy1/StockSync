from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy


from .models import ProductStockMoviment
from .forms import ProductStockMovimentForm


class StockExitMovement(LoginRequiredMixin, ListView):
    model = ProductStockMoviment
    template_name = 'moviments/moviment_list.html'
