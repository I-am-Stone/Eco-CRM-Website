from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    cart_data = ProductInventory.objects.prefetch_related("media_product_inventory").all()
    print(cart_data)
    context ={
        'cart':cart_data
    }
    print(context)
    
    return render(request,"inventory/cart.html", context)

def checkout(request):
    return render(request,"inventory/checkout.html")
