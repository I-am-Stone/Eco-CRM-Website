from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):

    cart = request.session.get('cart',[])

    if request.method == 'POST':
        product_id = request.post.get('product_id')
        quantity = int(request.POST.get('Quantity', 1))
    




    cart_data = ProductInventory.objects.prefetch_related("media_product_inventory").all()
    print(cart_data)
    context ={
        'cart':cart_data
    }
    if request.method == 'POST':
        Product_id = request.POST.get('')
        
    return render(request,"inventory/cart.html", context)

def checkout(request):
    return render(request,"inventory/checkout.html")
