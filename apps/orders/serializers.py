from rest_framework import serializers
from .models import CartMeta


class CartMetaSerializers(serializers.ModelSerializer):
    class Meta:
        model = CartMeta
        fields = '__all__'
