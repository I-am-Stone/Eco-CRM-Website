from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, "dashboard/side.html")


def add_product(request):
    return render(request, "dashboard/add_product.html")


def orders(request):
    return render(request, "dashboard/add_product.html")
