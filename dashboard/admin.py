from django.contrib import admin

from .models import *
# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_meta','item', 'total_price', 'status', 'created_at',)



@admin.register(OrderMeta)
class OrderMetaAdmin(admin.ModelAdmin):
    list_display = ('product_inventory','customer')