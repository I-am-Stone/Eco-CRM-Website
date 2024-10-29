from django.contrib import admin
from .models import *


# Registering models here

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['web_id', 'slug', 'name', 'description', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

    list_editable = ['name']


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


@admin.register(ProductAttributeValue)
class ProductAttributeValuesAdmin(admin.ModelAdmin):
    list_display = ['product_attribute', 'attribute_value']


@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display = ['sku', 'upc', 'product_type', 'product', 'is_active', 'retail_price', 'store_price', 'sale_price',
                    'weight', 'created_at', 'updated_at']
    list_editable = ['retail_price', 'sale_price', 'store_price']


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['product_inventory', 'image', 'alt_text', 'is_feature', 'created_at', 'updated_at']

    list_editable = ['image', 'alt_text']


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['product_inventory', 'last_checked', 'units', 'units_sold']


@admin.register(ProductAttributeValues)
class ValuesAdmin(admin.ModelAdmin):
    list_display = ['attributevalues', 'productinventory']


# admin.site.register(ProductType)
# admin.site.register(ProductInventory)
# admin.site.register(Brand)
# admin.site.register(ProductAttribute)
# admin.site.register(ProductAttributeValue)
# admin.site.register(Media)
# admin.site.register(Stock)
# admin.site.register(ProductAttributeValues)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'city', 'state', 'country', 'created_at', 'street')
    search_fields = ('name', 'email', 'phone')


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at', 'message')
    search_fields = ('name', 'email', 'subject')
