from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import ProductStock
from .forms import ProductStockForm
from moviments.forms import ProductStockMovimentForm


class ProductStockList(LoginRequiredMixin, ListView):
    template_name = 'stock/stock_list.html'
    model = ProductStock


class ProductStockCreate(LoginRequiredMixin, CreateView):
    template_name = 'stock/stock_form.html'
    model = ProductStock
    form_class = ProductStockForm
    success_url = reverse_lazy('stock:list')


class ProductStockUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'stock/stock_form.html'
    model = ProductStock
    form_class = ProductStockForm
    success_url = reverse_lazy('stock:list')


class ProductStockSub(LoginRequiredMixin, TemplateView):
    template_name = 'stock/stock_sub.html'

    def get_context_data(self, **kwargs):
        context = super(ProductStockSub, self).get_context_data(**kwargs)
        context['stock'] = get_object_or_404(ProductStock, pk=self.kwargs['pk'])
        context['form'] = ProductStockMovimentForm(self.request.POST or None)
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        stock = context['stock']
        form = context['form']
        if form.is_valid():
            form.instance.product_stock = stock
            form.instance.author = self.request.user
            moviment = form.save()
            stock.quantity = stock.quantity - moviment.quantity
            stock.save()
            return redirect(reverse_lazy('stock:sub', kwargs={'pk': self.kwargs['pk']}))
        return self.render_to_response(context)
