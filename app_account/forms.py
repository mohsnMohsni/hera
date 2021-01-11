from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-100 auth-input'
    }))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        'class': 'w-100 auth-input'
    }))


class SignUpForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input'}))

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'w-100 auth-input'}),
            'password': forms.PasswordInput(attrs={'class': 'w-100 auth-input'}),
            'full_name': forms.TextInput(attrs={'class': 'w-100 auth-input'}),
        }
