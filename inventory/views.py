from django.shortcuts import render, redirect
from inventory.models import *
from django.http import JsonResponse


def home(request):
    shop = ProductInventory.objects.prefetch_related("media_product_inventory").all()

    if request.method == "POST":
        if 'product_id' in request.POST:
            product_id = request.POST.get('product_id')
            quantity = request.POST.get('quantity')
            cart = request.session.get('cart', {})

            if product_id in cart:
                cart[product_id] += int(quantity)
            else:
                cart[product_id] = int(quantity)

            request.session['cart'] = cart


    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0

    for product_id, quantity in cart.items():
        product = ProductInventory.objects.prefetch_related("media_product_inventory").filter(pk=product_id).first()
        
        if product:
            item_total = product.retail_price * int(quantity)
            product_name = product.product.name
            media_info = [{'url': media.image, 'alt_text': media.alt_text} for media in product.media_product_inventory.all()]

            cart_items.append({
                'product': product,
                'quantity': quantity,
                'item_total': item_total,
                'product_name': product_name,
                'media_info': media_info
            })

            total_price += item_total

    context = {
        'products': shop,
        'cart_items': cart_items,
        'total_price': total_price
    }

    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart

    return render(request, "inventory/cart.html", context)





def checkout(request):
    return render(request, "inventory/checkout.html")


# def remove_from_cart(request):
#     if request.method == 'POST' and 'remove_item_id' in request.POST:
#         remove_item_id = request.POST.get('remove_item_id')
#         cart = request.session.get('cart', {})
#         if remove_item_id in cart:
#             del cart[remove_item_id]
#             request.session['cart'] = cart
#             return JsonResponse({'message': 'Item removed successfully'}, status=200)
#         else:
#             return JsonResponse({'error': 'Item not found in the cart'}, status=404)
#     else:
#         return JsonResponse({'error': 'Invalid request'}, status=400)
