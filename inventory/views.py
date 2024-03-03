from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,"inventory/cart.html")

def checkout(request):
    return render(request,"inventory/checkout.html")

