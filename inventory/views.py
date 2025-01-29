from django.shortcuts import render, redirect
from inventory.models import *
from dashboard.models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import ProductInventory
from .services.cart_service import CartService
from .services.order_service import CheckoutService
from .services.contact_service import ContactService

def home(request):
    """
    Home page
    :param request:
    :return:
    This sends the item details to the template of home page
    """
    
    shop = ProductInventory.objects.prefetch_related("media_product_inventory").all().order_by('id')  # Add ordering
    
    cart = CartService.add_product_to_carts(request)


    print(cart)
    paginator = Paginator(shop, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'cart_items':cart['cart_items'],
        'total_price':cart['total_price'],
    }

    return render(request, "inventory/product.html", context)

def remove_from_cart(request):
    CartService.remove_from_cart(request)
    return redirect('inventory:home')

def checkout(request):
    cart = CartService.add_product_to_carts(request)

    form_data, cust_id = CheckoutService.save_customer_data(request)
    # If request if post, save user data invoice and change progress

    context = {
        'step': request.GET.get('step', 'fill_info'),
        'form_data': form_data,
        'cust_id': cust_id,
        'cart_items':cart['cart_items'],
        'total_price':cart['total_price'],
    }
    return render(request, "inventory/checkout.html", context)




def buy_now(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        cart = {product_id: quantity}
        request.session['cart'] = cart
        return redirect('inventory:checkout')
    return redirect('inventory:home')


def contact(request):
    cart = CartService.add_product_to_carts(request)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        ContactService.create(name=name, email=email, subject=subject, message=message)
    context = {
        'cart_items':cart['cart_items'],
        'total_price':cart['total_price'],

    }

    return render(request, "inventory/contact.html",context)


def about(request):
    cart = CartService.add_product_to_carts(request)

    context = {
        'cart_items':cart['cart_items'],
        'total_price':cart['total_price'],

    }
    
    return render(request, "inventory/about.html",context)


def order_info(request):
    if request.method == "POST":
        cart: dict = request.session.get('cart', {})
        quantity = cart['1']
        print(cart, quantity)
        customer_id = request.POST.get('cust_id')

        for key, value in cart.items():
            product = ProductInventory.objects.prefetch_related("product").get(pk=key)
            
            CheckoutService.save_order_data(cust_id=customer_id, cart_items=cart, total_price=product.retail_price, product=stock, status=Order.status)    
            
            return redirect('dashboard:checkout')

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


