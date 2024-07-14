# forms.py
from django import forms
import re

class CustomerForm(forms.Form):
    email = forms.EmailField()
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    street = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    state = forms.CharField(max_length=100, required=False)
    zip = forms.CharField(max_length=20, required=False)
    country = forms.CharField(max_length=100, required=False)


    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?[0-9\s\-]+$', phone):  # Basic phone number validation
            raise forms.ValidationError('Invalid phone number')
        return phone
