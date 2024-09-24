from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import *
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.hashers import make_password


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
    return render(request, "dashboard/products.html", context)


def orders(request):
    orders_collection = Order.objects.select_related('customer').all().order_by('-created_at')
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

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            # Generic error message for invalid credentials
            messages.error(request, "Invalid username or password")
            return redirect('signin')

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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        status = request.POST.get('status')  # Assuming 'status' refers to whether the user is a staff member or not.
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists.')
            else:
                is_staff = True if status == 'on' else False  # Change 'on' based on the value sent from the form
                user = User.objects.create_user(username=username, email=email, password=password1, is_staff=is_staff)
                user.save()
                messages.success(request, 'User created successfully.')
                return redirect('setting')
        else:
            messages.error(request, 'Passwords do not match.')

    user_details = User.objects.all()
    context = {
        'user': user_details
    }
    return render(request, "dashboard/setting.html", context)


def inbox(request):
    msgs = ContactForm.objects.all()
    context = {
        'info': msgs
    }
    return render(request, "dashboard/inbox.html", context)


def categories(request):
    cate = Category.objects.all()
    context = {
        'items':cate
    }
    return render(request, "dashboard/categories.html", context)


def stocks(request):
    cate = Stock.objects.all()
    context = {
        'items':cate
    }
    return render(request, "dashboard/stocks.html", context)


def notification(request):
    notification = Notification.objects.all()

    context={
        'notify':notification
    }
    return render(request, "dashboard/notification.html", context)