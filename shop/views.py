from django.shortcuts import render
from shop.models import Product


def shop(request):
    return render(request, 'shop.html', {
        'products': Product.objects.all(),
    })
