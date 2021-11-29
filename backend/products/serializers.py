
from rest_framework import serializers


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=400)
    image = serializers.ImageField()
    in_stock = serializers.BooleanField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)


class AllProductSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=400)
    image = serializers.ImageField()
    in_stock = serializers.BooleanField()
    price = serializers.DecimalField(max_digits=6, decimal_places=2)