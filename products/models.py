from django.db import models

from brands.models import Brand
from categories.models import Category

class Product(models.Model):

    name = models.CharField('Nome', max_length=120)
    description = models.TextField('Descrição', null=True, blank=True)
    brands = models.ManyToManyField(Brand, verbose_name='Marca', blank=True)
    category = models.ForeignKey(Category, verbose_name='Categoria', null=True, blank=True, on_delete=models.SET_NULL)

    # timestamps
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
