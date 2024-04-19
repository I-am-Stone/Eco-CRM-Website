from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    cart_data = ProductInventory.objects.all().select_related("product_inventory")
    context ={
        'cart':cart_data
    }
    
    return render(request,"inventory/cart.html", context)

def checkout(request):
    return render(request,"inventory/checkout.html")
