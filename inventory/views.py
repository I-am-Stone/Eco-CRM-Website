from django.shortcuts import render, redirect, get_object_or_404
from inventory.models import *
from django.http import JsonResponse
import json


def get_cart_items(cart):
    cart_items = []
    total_price = 0

    product_ids = cart.keys()
    products = ProductInventory.objects.prefetch_related("media_product_inventory").filter(pk__in=product_ids)

    for product in products:
        quantity = cart[str(product.pk)]
        item_total = product.retail_price * quantity
        product_name = product.product.name
        media_info = [{'url': media.image, 'alt_text': media.alt_text} for media in product.media_product_inventory.all()]

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
            'product_name': product_name,
            'media_info': media_info,
            'retail_price': product.retail_price,
        })

        total_price += item_total

    return cart_items, total_price


def home(request):
    shop = ProductInventory.objects.prefetch_related("media_product_inventory").all()

    if request.method == "POST":
        if 'product_id' in request.POST:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            cart = request.session.get('cart', {})

            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity

            request.session['cart'] = cart

    cart = request.session.get('cart', {})
    cart_items, total_price = get_cart_items(cart)

    context = {
        'products': shop,
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, "inventory/cart.html", context)

def checkout(request):
    cart = request.session.get('cart', {})
    cart_items, total_price = get_cart_items(cart)

    context = {
        'cart_items': cart_items,
    }
    return render(request, "inventory/checkout.html", context)


def remove_from_cart(request):
    if request.method == "POST":
        remove_item_id = request.POST.get('remove_item_id')
        cart = request.session.get('cart', {})
        
        if remove_item_id in cart:
            del cart[remove_item_id]
            request.session['cart'] = cart
    
    return redirect('home')


def buy_now(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        cart = {product_id: quantity}
        request.session['cart'] = cart

        return redirect('checkout')
    return redirect('home')




def customerInfo(request):
    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('customer')
        street = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip = request.POST.get('zip')
        country = request.POST.get('country')










