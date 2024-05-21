from django.shortcuts import render, redirect
from django.http import JsonResponse
from inventory.models import *  # Ensure this import matches your actual model location

def home(request):
    products = ProductInventory.objects.prefetch_related("media_product_inventory").all()
    
    context = {
        'products': products
    }        

    return render(request, "inventory/cart.html", context)

def add_to_cart(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')

        cart = request.session.get('cart', {})
        print(request.session.get('cart', {}))

        if product_id in cart:
            cart[product_id] += int(quantity)
        else:
            cart[product_id] = int(quantity)
        
        request.session['cart'] = cart

        return JsonResponse({'message': 'Item added to cart successfully'})
    else:
        return redirect('home')

def cart_details(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    product_ids = cart.keys()
    print(product_ids)
    products = ProductInventory.objects.filter(id__in=product_ids)

    print(products)

    for product in products:
        quantity = cart[str(product.id)]
        item_total = product.retail_price * quantity
        total_price += item_total

        cart_items.append({
            'product_id': product.id,
            'product_name': product.name,
            'product_description': product.description,
            'quantity': quantity,
            'item_total': item_total,
        })

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    print(context)
    return render(request, "inventory/cart.html", context)

def checkout(request):
    return render(request, "inventory/checkout.html")
