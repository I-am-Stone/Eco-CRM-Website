from django.shortcuts import render, redirect
from inventory.models import *
from .form import CustomerForm
from django.urls import reverse
from dashboard.models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import ProductInventory
from django.core.mail import send_mail
from django.conf import settings
from .services.cart_service import CartService 


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
    cart = CartService.remove_from_cart(request)
    return redirect('inventory:home')

def checkout(request):
    form_data = {}
    cust_id = None
    # If request if post, save user data invoice and change progress
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            phone = form.cleaned_data['phone']
            zip_code = form.cleaned_data['zip']
            country = form.cleaned_data['country']

            new_customer = Customer(
                email=email,
                name=name,
                phone=phone,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code,
                country=country
            )
            new_customer.save()
            cust_id = new_customer.pk  # Set id of just inserted customer
            form_data = form.cleaned_data

            
    context = {
        'step': request.GET.get('step', 'fill_info'),
        'form_data': form_data,
        'cust_id': cust_id
    }
    return render(request, "inventory/checkout.html", context)




def buy_now(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        cart = {product_id: quantity}
        request.session['cart'] = cart
        print(cart)
        return redirect('inventory:checkout')
    return redirect('inventory:home')


def contact(request):
    cart = CartService.add_product_to_carts(request)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contest = ContactForm(
            email=email,
            name=name,
            subject=subject,
            message=message,
        )
        contest.save()
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
            stock = Stock.objects.select_for_update().get(product_inventory=product)

            order = Order(
                item=product.product.name,
                total_price=product.retail_price,
                item_count=value,
                product_inventory=product,
                customer_id=customer_id,
                status=Order.status,
            )
            order.save()

            stock.units -= int(value)
            stock.save()
        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


