from django.contrib import admin
from shop.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'photo', 'item_number')

admin.site.register(Product, ProductAdmin)
