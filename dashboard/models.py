from django.db import models
from django.utils.translation import gettext_lazy as _
from inventory.models import ProductInventory, Customer


class Order(models.Model):
    item = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_PENDING = 'Pending'
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

    item_count = models.IntegerField(null=True, blank=True)
    product_inventory = models.ForeignKey(
        ProductInventory,
        related_name="orders",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )
    customer = models.ForeignKey(
        Customer,
        related_name="orders",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"Order(id={self.id}, status={self.status})"


