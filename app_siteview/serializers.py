from app_product.models import Product, Category
from rest_framework import serializers


class ProductSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'slug')


class CategorySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
