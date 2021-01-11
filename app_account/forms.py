from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .validators import password_validator, name_validator


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

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        password_validator(password, password2)
        return password2

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
        name_validator(full_name)
        return full_name


class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input'}))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input'}))

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        password_validator(password, password2)
        return password2
