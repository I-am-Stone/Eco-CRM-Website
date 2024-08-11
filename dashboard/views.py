from django.shortcuts import render
from inventory.models import *


# Create your views here.
def dashboard(request):
    graph_data = ProductInventory.objects.all().order_by('id')

    context = {
        'graph_data': graph_data
    }
    return render(request, "dashboard/side.html",context)


def add_product(request):
    return render(request, "dashboard/add_product.html")


def orders(request):
    return render(request, "dashboard/order.html")
