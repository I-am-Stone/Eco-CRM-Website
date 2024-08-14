from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_product', views.add_product, name='add_product'),
    path('orders', views.orders, name='orders'),
    path('update_order_status', views.update_order_status, name='update_order_status'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

