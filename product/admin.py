from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    List_display = ['category', 'name', 'value']
admin.site.register(Product, ProductAdmin)
