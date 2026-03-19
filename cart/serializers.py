from rest_framework import serializers
from .models import Cart
from products.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'product', 'product_id', 'quantity']
        read_only_fields = ['user', 'product']