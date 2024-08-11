from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('item', 'total_price', 'status', 'created_at','item_count', 'product_inventory', 'customer')
