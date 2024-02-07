from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class user(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("brand name"),
        help_text=_("format: required, unique, max-255"),
    )
