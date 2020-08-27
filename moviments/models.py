from django.db import models

from stock.models import ProductStock
from accounts.models import User


class ProductStockMoviment(models.Model):

    class ProductStockMovimentType(models.IntegerChoices):
        SALE = 0, 'Venda'
        INTERNAL_CONSUME = 1, 'Consumo Interno'
        DISCARD = 2, 'Descarte'
        LOSS = 3, 'Extravio'

    product_stock = models.ForeignKey(ProductStock, verbose_name='Produto em estoque', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.SET_NULL)
    moviment_type = models.IntegerField('Tipo de movimentação', choices=ProductStockMovimentType.choices, default=ProductStockMovimentType.SALE)
    # timestamps
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return str(self.created_at)

    class Meta:
        verbose_name = 'Movimentação de produto em estoque'
        verbose_name_plural = 'Movimentações de produtos em estoque'
        ordering = ['-created_at']
