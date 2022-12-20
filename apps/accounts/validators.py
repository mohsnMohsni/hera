from django.forms import ValidationError
from .models import User


def name_validator(name):
    """
    Check the name, If it have been started by int
    return ValidationError.
    """
    if name[0] == int:
        raise ValidationError(
            'name should be start with [a-z]'
        )


def password_validator(password1, password2):
    """
    Check passwords, if len of passwords are less than 8 char
    or passwords are not same
    return ValidationError.
    """
    if len(password1) < 8:
        raise ValidationError(
            'password is similar'
        )
    if password1 != password2:
        raise ValidationError(
            'passwords are not match'
        )


def user_password_validator(user_email, password):
    """
    Find user and check user password is same as that password has been enter.
    """
    try:
        user = User.objects.get(email=user_email)
    except User.DoesNotExist:
        raise ValidationError(
            'Something is wrong'
        )
    if user.check_password(password) is False:
        raise ValidationError(
            'Current Password is not true'
        )
