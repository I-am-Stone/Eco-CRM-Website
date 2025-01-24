from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'inventory'
urlpatterns = [
                  path('', views.home, name='home'),
                  path('checkout', views.checkout, name='checkout'),
                  path('buy_now/', views.buy_now, name='buy_now'),
                  path('order/', views.order_info, name='order_info'),
                  path('contact/', views.contact, name='contact'),
                  path('aboutus/', views.about, name='about'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
