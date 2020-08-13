from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=120)

    # timestamps
    created_at = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_at = models.DateTimeField('Data de atualização', auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
