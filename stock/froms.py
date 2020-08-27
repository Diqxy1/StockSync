from django import forms

from .models import ProductStock


class ProductStockForm(forms.ModelForm):
    class Meta:
        model = ProductStock
        fields = ['product', 'brand', 'quantity', 'lot', 'validity', 'price', 'coast']
