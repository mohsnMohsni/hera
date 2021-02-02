from django import forms
from .models import Shop


class AddShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('slug', 'name', 'detail', 'image', 'user')
        widgets = {
            'user': forms.TextInput(attrs={'hidden': '', 'value': '0'},),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file mt-2 pt-1'}),
        }
