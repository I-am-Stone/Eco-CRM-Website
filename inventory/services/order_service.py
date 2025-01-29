from inventory.form import CustomerForm
from dashboard.models import Order, Customer

class CheckoutService:

    @classmethod
    def save_customer_data(cls,request):
        form_data = {}
        cust_id = None
        # If request if post, save user data invoice and change progress
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
        return form_data, cust_id
    @staticmethod
    def save_order_data(cust_id, cart_items, total_price, product,status):
        new_order = Order(
            customer_id=cust_id, 
            item_count=len(cart_items), 
            total_price=total_price,
            product_inventory=product,
            status=status,
            )
        new_order.save()
        for item in cart_items:
            new_order.items.add(item)

