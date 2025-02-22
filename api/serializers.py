from rest_framework import serializers
from .models import Product, Order, OrderItem


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'stock',
            'image',
            'in_stock'
        ]

    def validate_name(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Price field must be greater then 0.'
            )
        return value


class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField (max_digits=10, decimal_places=2, source='product.price')
    class Meta:
        model = OrderItem
        fields = [
            'product_name',
            'product_price',
            'quantity',
            'item_subtotal',
        ]



class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = [
            'order_id',
            'user',
            'status',
            'created_at',
            'items',
            'total_price',
        ]

    def get_total_price(self, obj):
        order_items = obj.items.all()
        return sum(order_item.item_subtotal for order_item in order_items)




class ProductInfoSerializer(serializers.Serializer):
     products = ProductSerializer(many=True)
     count    = serializers.IntegerField()
     max_price = serializers.FloatField()
