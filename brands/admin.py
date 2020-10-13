from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display =(
        '__str__',
        'name',
        'created_at',
        'updated_at',
    )
    search_fields = ('name',)
