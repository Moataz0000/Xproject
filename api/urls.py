from django.urls import path
from .views import (
    prodcut_list,
    product_detail,
    order_list,
)


app_name = 'products'

urlpatterns = [
    path('products/', prodcut_list, name='product'),
    path('products/<int:pk>/', product_detail, name='product_detail'),
    path('orders/', order_list, name='order_list')

]