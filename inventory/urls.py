from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                #   path('cart/', views.add_product_to_carts, name='cart'),
                  path('checkout', views.checkout, name='checkout'),
                #   path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
                  path('buy_now/', views.buy_now, name='buy_now'),
                  # path('customerInfo/', views.customer_info, name='customerInfo'),
                  path('order/', views.order_info, name='order_info'),
                  path('contact/', views.contact, name='contact'),
                  path('aboutus/', views.about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
