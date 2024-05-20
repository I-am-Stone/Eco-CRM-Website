from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

import json


def home(request):
    cart_data = ProductInventory.objects.prefetch_related("media_product_inventory").all()
    

    context = {
        'cart': cart_data
    }        

    return render(request, "inventory/cart.html", context)

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        cart = request.session.get('cart',{})

        if product_id in cart:
            cart[product_id] += int(quantity)
        else:
            cart[product_id] = int(quantity)
        
        request.session['cart'] = cart

        return JsonResponse({'message': 'Item added to cart successfully'})
    else:
        return redirect('product_list')
    
def cart_details(request):
    cart = request.session.get('cart',{})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.itemss():
        product = ProductInventory.objects.get(pk=product_id).all()
        total_price += product.retail_price *quantity

        cart_items.append({
            'product':product,
            'quantity':quantity,
            'total_price':total_price
        })
    
    context = {
        'cart_items':cart_items
    }
    return render(request, "inventory/cart.html", context)




def checkout(request):
    return render(request,"inventory/checkout.html")
