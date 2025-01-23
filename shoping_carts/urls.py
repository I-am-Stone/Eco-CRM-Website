from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
                  path('cart/', views.add_product_to_carts, name='cart'),
                  path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
              ]