# Generated by Django 3.1 on 2020-10-14 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_auto_20201014_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productstock',
            name='new_quantity',
            field=models.PositiveIntegerField(default=0, null=True, verbose_name='Quantidade no estoque'),
        ),
    ]
