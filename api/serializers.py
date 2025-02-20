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
            'image'
        ]

    def validate_name(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Price field must be greater then 0.'
            )
        return value