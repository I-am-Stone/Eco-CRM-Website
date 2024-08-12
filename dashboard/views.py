from django.shortcuts import render
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
    orders = Order.objects.all()

    for order in orders:
        custome_name = order.customer
        count = order.item_count
        item = order.item
        status = order.status
        date = order.created_at
        price = order.total_price
        cust_id = order.customer.pk

        orders_data.append({
            'pk':cust_id,
            'customer':custome_name,
            'count':count,
            'product':item,
            'status':status,
            'order_date':date,
            'cost':price
        })
    context = {
        'orders': orders_data
    }
    return render(request, "dashboard/order.html",context)
