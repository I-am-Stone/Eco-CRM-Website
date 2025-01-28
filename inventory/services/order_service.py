from inventory.form import CustomerForm
from dashboard.models import *

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

