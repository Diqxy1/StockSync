from django.db import models

from products.models import Product
from brands.models import Brand
from accounts.models import User

class ProductStock(models.Model):
    product = models.ForeignKey(Product, verbose_name='Produto', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, verbose_name='Marca', null=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField('Quantidade')
    new_quantity = models.PositiveIntegerField('Quantidade no estoque')
    lot = models.CharField('Lote', max_length=100)
    validity = models.DateField('Validade', null=True, blank=True)
    price = models.DecimalField('Preço', max_digits=9, decimal_places=2)
    coast = models.DecimalField('Custo', max_digits=9, decimal_places=2)
    author = models.ForeignKey(User, verbose_name='Autor', null=True, on_delete=models.SET_NULL)
    # timestamps
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.lot

    class Meta:
        verbose_name = 'Produto em estoque'
        verbose_name_plural = 'Produtos em estoque'


    @property
    def empyt_quantity(self):
        if self.new_quantity == 0:
            self.new_quantity = self.quantity
        return self.new_quantity
