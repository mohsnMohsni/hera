from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .validators import password_validator, name_validator


class SignInForm(AuthenticationForm):
    """
    Form that related to Login(Sign In) view.
    This form use Authentication form and override it and add widget to fields.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'w-100 auth-input', 'autofocus': ''
    }))
    password = forms.CharField(strip=False, widget=forms.PasswordInput(attrs={
        'class': 'w-100 auth-input'
    }))


class SignUpForm(forms.ModelForm):
    """
    Form that related to Register(Sign Up) view and User model.
    Get three fields for register the user with custom widgets.
    """
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input'}))

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'w-100 auth-input', 'autofocus': ''}),
            'password': forms.PasswordInput(attrs={'class': 'w-100 auth-input'}),
            'full_name': forms.TextInput(attrs={'class': 'w-100 auth-input'}),
        }

    def clean_password2(self):
        """
        This method for validate the passwords by user password_validator function.
        If not valid return an ValidationError.
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        password_validator(password, password2)
        return password2

    def clean_full_name(self):
        """
        This method for validate the full_name by user name_validator function.
        If not valid return an ValidationError.
        """
        full_name = self.cleaned_data.get('full_name')
        name_validator(full_name)
        return full_name


class ChangePasswordForm(forms.Form):
    """
    Form that related to ChangePassword view and user model.
    Get two field to set new password
    """
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input', 'autofocus': ''}))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input'}))

    def clean_password2(self):
        """
        This method for validate the passwords by user password_validator function.
        If not valid return an ValidationError.
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        password_validator(password, password2)
        return password2
