from django.http import  JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer, ProductInfoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max
@api_view(http_method_names=['GET'])
def prodcut_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True )
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def product_detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def order_list(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(http_method_names=['GET'])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        "products": products,
        "count": len(products ),
        "max_price": products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)