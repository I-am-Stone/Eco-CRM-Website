from .models import *
from django.shortcuts import render, redirect
import json

# Create your views here.



def home(request):
    cart_data = ProductInventory.objects.prefetch_related("media_product_inventory").all()
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product_name = request.POST.get('product_name')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity', 1)

        # Create a dictionary to store item data
        item_data = {
            'product_id': product_id,
            'product_name': product_name,
            'price': price,
            'quantity': quantity
        }

        # Initialize an empty list if 'cart' does not exist in session
        cart = request.session.get('cart', [])
        cart.append(item_data)

        request.session['cart'] = json.dumps(cart)

    context = {
        'cart': cart_data
    }

    return render(request, "inventory/cart.html", context)


def checkout(request):
    return render(request,"inventory/checkout.html")
