from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator


# Create your views here.
def dashboard(request):
    graph_data = ProductInventory.objects.all().order_by('id')

    context = {
        'graph_data': graph_data
    }
    return render(request, "dashboard/side.html", context)


def add_product(request):
    items = []
    products = ProductInventory.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for product in products:
        product_name = product.product.name
        price = product.retail_price
        product_description = product.product.description
        added_date = product.created_at
        active_status = product.is_active
        product_type = product.product_type
        brand = product.brand

        items.append({
            'product_name': product_name,
            'product_price': price,
            'product_description': product_description,
            'added_date': added_date,
            'active_status': active_status,
            'product_type': product_type,
            'brand': brand
        })

    context = {
        'items': items,
        'page_obj': page_obj
    }
    return render(request, "dashboard/add_product.html", context)


def orders(request):
    orders_collection = Order.objects.select_related('customer').all()
    paginator = Paginator(orders_collection, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'orders': orders_collection,
        'page_obj': page_obj
    }
    return render(request, "dashboard/order.html", context)


def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('signin')
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('signin')
        else:
            login(request, user)
            return redirect('dashboard')

    return render(request, "dashboard/sign_in.html")


def order_status(request, order_id):
    if request.method == 'POST':
        print(f"Attempting to update order with id: {order_id}")
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()

        return redirect('orders')

    return render(request, "dashboard/order_status.html", {'order': order_id})


def setting(request):
    return render(request, "dashboard/setting.html")


