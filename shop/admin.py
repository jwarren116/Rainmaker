from django.contrib import admin
from shop.models import Product, Cart


class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description', 'price', 'photo', 'item_number')


class CartAdmin(admin.ModelAdmin):
    model = Cart


admin.site.register(Product, ProductAdmin)
admin.site.register(Cart, CartAdmin)
