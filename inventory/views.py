from django.shortcuts import render

# Create your views here.


def home(request):
    # context = {}
    return render(request,"inventory/cart.html")

def checkout(request):
    # context = {}
    return render(request,"inventory/checkout.html")