from django.shortcuts import render, redirect
from django.http import JsonResponse
from inventory.models import *


def home(request):
    products = ProductInventory.objects.prefetch_related("media_product_inventory").all()
    
    context = {
        'products': products
    }

    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        print(product_id)



        cart = request.session.get('cart', {})

        if product_id in cart:
            cart[product_id] += int(quantity)
        else:
            cart[product_id] = int(quantity)

        request.session['cart'] = cart
    
    cart = request.session.get('cart', {})
    print(request.session.get('cart',{}))
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
            product = ProductInventory.objects.prefetch_related("media_product_inventory").get(pk=product_id)
            item_total = product.retail_price * int(quantity)
            total_price += item_total
            print(product)

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total
            })

    context = {
        'products': products,
        'cart_items': cart_items,
        'total_price': total_price
    }
    print(context)
    return render(request, "inventory/cart.html",context)




def checkout(request):
    return render(request, "inventory/checkout.html")
