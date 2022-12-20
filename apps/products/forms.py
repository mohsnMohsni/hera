from .models import Shop, Product, ShopProduct, ProductMeta, Brand, Category
from django.db.utils import OperationalError
from django.db import connection
from django import forms


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('slug', 'name', 'detail', 'image', 'user')
        widgets = {
            'user': forms.TextInput(attrs={'hidden': '', 'value': '0'}, ),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file mt-2 pt-1'}),
        }


class ShopProductForm(forms.ModelForm):
    price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        all_tables = connection.introspection.table_names()
        BRAND_CHOICE = Brand.objects.all() if len(all_tables) > 0 else []
        CATEGORY_CHOICE = Category.objects.all() if len(all_tables) > 0 else []
        model = Product
        exclude = ('crop_it', 'cropping')
        widgets = {
            'brand': forms.Select(attrs={'class': 'form-control'}, choices=BRAND_CHOICE),
            'category': forms.Select(attrs={'class': 'form-control'}, choices=CATEGORY_CHOICE),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file mt-2 pt-1'}),
        }
