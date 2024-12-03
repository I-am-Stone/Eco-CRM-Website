from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.signin, name='signin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('products', views.add_product, name='add_product'),
    path('setting', views.setting, name='setting'),
    path('orders', views.orders, name='orders'),
    path('categories', views.categories, name='categories'),
    path('stocks', views.stocks, name='stocks'),
    path('order_status/<int:order_id>/', views.order_status, name='order_status'),
    path('notification', views.notification, name='notification'),
    path('aboutus/', views.inbox, name='inbox'),
    path('basic_details/', views.product_data_collector, name='basic_details'),
    path('inventory/', views.inventory_data_collector, name='inv_details'),
    path('media/', views.media_collection, name='media'),
    path('invoice/', views.invoice, name='invoice'),
    path('add_product/', views.add, name='add'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

