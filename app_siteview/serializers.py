from app_product.models import Product, Category, ShopProduct
from rest_framework import serializers


class ShopProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopProduct
        fields = ('id',)


class ProductSearchSerializer(serializers.ModelSerializer):
    shop_product = ShopProductSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = ('name', 'slug', 'detail', 'shop_product')


class CategorySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug', 'detail')
