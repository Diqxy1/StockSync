from django import forms

from .models import ProductStockMoviment


class ProductStockMovimentForm(forms.ModelForm):

    class Meta:
        model = ProductStockMoviment
        fields = ['quantity', 'moviment_type']
