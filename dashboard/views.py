from django.shortcuts import render, get_object_or_404, redirect
from inventory.models import *
from .models import *


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
        'items': items
    }
    return render(request, "dashboard/add_product.html", context)


def orders(request):
    orders_data = []
    orders_collection = Order.objects.select_related('customer').all()

    for order in orders_collection:
        customer_name = order.customer.name  # Assuming there's a name field in the Customer model
        count = order.item_count
        item = order.item
        status = order.STATUS_PENDING
        date = order.created_at
        price = order.total_price
        cust_id = order.customer.pk
        address = f"{order.customer.street}, {order.customer.city}, {order.customer.state}, {order.customer.zip_code}"
        order_key = Order.pk

        orders_data.append({
            'key': order_key,
            'pk': cust_id,
            'customer': customer_name,
            'count': count,
            'product': item,
            'status': status,  # Use the actual status from the order
            'order_date': date,
            'cost': price,
            'address': address,
        })

    context = {
        'orders': orders_data
    }
    print(orders_collection)
    return render(request, "dashboard/order.html", context)


def signin(request):
    return render(request, "dashboard/sign_in.html")


def update_order_status(request, order_id):
    if request.method == 'POST':
        print(f"Attempting to update order with id: {order_id}")
        order = get_object_or_404(Order, id=order_id)
        new_status = request.POST.get('status')
        if new_status:
            order.status = new_status
            order.save()

        return redirect('orders')
