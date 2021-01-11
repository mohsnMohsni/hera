from django import forms
from django.contrib.auth.forms import AuthenticationForm


class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-100 auth-input'
    }))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        'class': 'w-100 auth-input'
    }))
