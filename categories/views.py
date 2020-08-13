from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Category


class CategoryList(LoginRequiredMixin, ListView):
    model = Category


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('categories:list')
