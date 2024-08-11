from django.db import models
from inventory.models import *

class OrderMeta(models.Model):
    product = models.ForeignKey(
        Product, related_name="order_meta_products", on_delete=models.PROTECT
    )
    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="order_meta_product_inventories",
        on_delete=models.PROTECT,
    )
    customer = models.ForeignKey(
        Customer,
        related_name="order_meta_customers",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"OrderMeta(product_id={self.product.id}, customer_id={self.customer.id})"


class Order(models.Model):
    order_meta = models.ForeignKey(
        OrderMeta,
        related_name="orders",
        on_delete=models.PROTECT,
    )
    item = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    STATUS_PENDING = 'PENDING'
    STATUS_PROCESSING = 'PROCESSING'
    STATUS_COMPLETED = 'COMPLETED'
    STATUS_CANCELLED = 'CANCELLED'
    
    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_PROCESSING, 'Processing'),
        (STATUS_COMPLETED, 'Completed'),
        (STATUS_CANCELLED, 'Cancelled'),
    ]
    
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING
    )

    def __str__(self):
        return f"Order(id={self.id}, status={self.status})"
