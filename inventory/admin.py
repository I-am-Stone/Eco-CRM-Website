from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['web_id', 'slug', 'name', 'description', 'created_at', 'updated_at']
    prepopulated_fields = {'slug':('name',)}

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display =['name', 'description']

@admin.register(ProductAttributeValue)
class ProductAttributeValuesAdmin(admin.ModelAdmin):
    list_display = ['product_attribute','attribute_value']

@admin.register(ProductInventory)
class ProductInventoryAdmin(admin.ModelAdmin):
    list_display =['sku','upc','product_type','product','is_active','retail_price','store_price','sale_price','weight','created_at','updated_at']

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ['product_inventory','image','alt_text','is_feature','created_at','updated_at']

@admin.register(Stock)
class stockAdmin(admin.ModelAdmin):
    list_display = ['product_inventory', 'last_checked', 'units','units_sold']

@admin.register(ProductAttributeValues)
class ValuesAdmin(admin.ModelAdmin):
    list_display = ['attributevalues','productinventory']

# admin.site.register(ProductType)
# admin.site.register(ProductInventory)
# admin.site.register(Brand)
# admin.site.register(ProductAttribute)
# admin.site.register(ProductAttributeValue)
# admin.site.register(Media)
# admin.site.register(Stock)
# admin.site.register(ProductAttributeValues)
