from django.shortcuts import render
from shop.models import Product


def shop(request):
    return render(request, 'shop.html', {
        'products': Product.objects.all(),
    })


def view_cart(request):
    cart = request.session.get('cart', {})
    return render(request, 'cart.html', {
        'cart': cart,
    })


def add_to_cart(request, item_id, quantity):
    cart = request.session.get('cart', {})
    cart[item_id] = quantity
    request.session['cart'] = cart
    return render(request, 'cart.html', {
        'cart': cart,
    })
