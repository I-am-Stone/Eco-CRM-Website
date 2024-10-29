from django.shortcuts import render, redirect
from inventory.models import *
from .form import CustomerForm
from django.urls import reverse
from dashboard.models import *
from django.http import JsonResponse
from .utils import create_notification
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import ProductInventory


def get_cart_items(cart):
    cart_items = []
    total_price = 0

    product_ids = cart.keys()
    products = ProductInventory.objects.prefetch_related("media_product_inventory").filter(pk__in=product_ids)
    for product in products:
        quantity = cart[str(product.pk)]
        item_total = product.retail_price * quantity
        product_name = product.product.name
        media_info = [{'url': media.image, 'alt_text': media.alt_text} for media in
                      product.media_product_inventory.all()]

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total,
            'product_name': product_name,
            'media_info': media_info,
            'retail_price': product.retail_price,
        })

        total_price += item_total

    return cart_items, total_price


def home(request):
    """
    Home page
    :param request:
    :return:
    This sends the item details to the template of home page
    """
    shop = ProductInventory.objects.prefetch_related("media_product_inventory").all()

    if request.method == "POST":
        if 'product_id' in request.POST:
            product_id = request.POST.get('product_id')
            quantity = int(request.POST.get('quantity', 1))
            cart = request.session.get('cart', {})

            if product_id in cart:
                cart[product_id] += quantity
            else:
                cart[product_id] = quantity

            request.session['cart'] = cart

    cart = request.session.get('cart', {})
    cart_items, total_price = get_cart_items(cart)

    paginator = Paginator(shop, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'cart_items': cart_items,
        'total_price': total_price,
    }

    return render(request, "inventory/cart.html", context)


def checkout(request):
    cart = request.session.get('cart', {})
    cart_items, total_price = get_cart_items(cart)
    form = None
    form_data = {}
    cust_id = None
    # If request if post, save user datinvoicea and change progress
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Process the valid form data
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            phone = form.cleaned_data['phone']
            zip_code = form.cleaned_data['zip']
            country = form.cleaned_data['country']

            new_customer = Customer(
                email=email,
                name=name,
                phone=phone,
                street=street,
                city=city,
                state=state,
                zip_code=zip_code,
                country=country
            )
            new_customer.save()
            cust_id = new_customer.pk  # Set id of just inserted customer
            form_data = form.cleaned_data

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
        'step': request.GET.get('step', 'fill_info'),
        'form_data': form_data,
        'cust_id': cust_id
    }
    return render(request, "inventory/checkout.html", context)


def remove_from_cart(request):
    if request.method == "POST":
        remove_item_id = request.POST.get('remove_item_id')
        cart = request.session.get('cart', {})

        if remove_item_id in cart:
            del cart[remove_item_id]
            request.session['cart'] = cart

    return redirect('home')


def buy_now(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))

        cart = {product_id: quantity}
        request.session['cart'] = cart
        return redirect('checkout')
    return redirect('home')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contest = ContactForm(
            email=email,
            name=name,
            subject=subject,
            message=message,
        )
        contest.save()
        create_notification(
            f"New order placed for {contest.email} by {contest.email}",
            notification_type='message',
            link=f'/dashboard/orders/{contest.pk}/'  # Adjust this URL as needed
        )

    return render(request, "inventory/contact.html")


def about(request):
    return render(request, "inventory/about.html")


def order_info(request):
    if request.method == "POST":
        cart: dict = request.session.get('cart', {})
        quntity = cart['1']
        print(cart, quntity)
        customer_id = request.POST.get('cust_id')

        for key, value in cart.items():
            product = ProductInventory.objects.prefetch_related("product").get(pk=key)
            stock = Stock.objects.select_for_update().get(product_inventory=product)

            total_price = product.retail_price * quntity

            order = Order(
                item=product.product.name,
                total_price=total_price,
                item_count=value,
                product_inventory=product,
                customer_id=customer_id,
                status=Order.status,
            )
            order.save()

            stock.units -= int(value)
            stock.save()
            create_notification(
                f"New order placed for {order.item} by {order.customer}",
                notification_type='order',
                link=reverse('orders')  # Adjust this URL as needed
            )

        return JsonResponse({'status': 'success'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
