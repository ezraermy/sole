from django.conf import settings
from django.shortcuts import render, redirect
from .cart import Cart

# Create your views here.
def cart_detail(request):
    cart = Cart(request)
    productsstring = ''

    print(cart)

    for item in cart:
        product = item['product']
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s'}," % (product.id, product.title, product.price, item['quantity'], item['total_price'])

        productsstring = productsstring + b

    context = {
        'cart': cart,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'productsstring': productsstring,
    }

    return render(request, 'cart.html', context)

def success(request):
    cart = Cart(request)
    cart.clear()
    
    return render(request, 'success.html')
