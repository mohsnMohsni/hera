from .validators import password_validator, name_validator, user_password_validator
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Address
from django import forms


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
    user_email = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'hidden': ''}))
    current_password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input', 'autofocus': ''}))
    password = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input'}))
    password2 = forms.CharField(max_length=100, required=True, widget=forms.PasswordInput(
        attrs={'class': 'w-100 auth-input'}))

    def clean_current_password(self):
        """
        Get user email and current_password from form
        and validate it.
        """
        user_email = self.cleaned_data.get('user_email')
        current_password = self.cleaned_data.get('current_password')
        user_password_validator(user_email, current_password)
        return current_password

    def clean_password2(self):
        """
        validate the passwords by user password_validator function.
        If not valid return an ValidationError.
        """
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        password_validator(password, password2)
        return password2


class AddAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ('user',)
        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'street': forms.TextInput(attrs={'class': 'form-control'}),
            'alley': forms.TextInput(attrs={'class': 'form-control'}),
            'no': forms.NumberInput(attrs={'class': 'form-control'}),
            'postal_code': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'phone', 'avatar')
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'autofocus': ''}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control-file mt-2 pt-1'}),
        }
