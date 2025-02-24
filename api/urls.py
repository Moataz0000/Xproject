from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    OrderListView,
    UserOrderListView,
    product_info,
)


app_name = 'products'

urlpatterns = [

    path('products/', ProductListView.as_view(), name='product'),
    path('products/<int:product_id>/', ProductDetailView.as_view(), name='product_detail'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('product-info/', product_info, name='product_info'),
    path('user-orders/', UserOrderListView.as_view(), name='user_orders')

]