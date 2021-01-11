from django.forms import ValidationError


def name_validator(name):
    if name[0] == int:
        raise ValidationError(
            'name should be start with [a-z]'
        )


def password_validator(password1, password2):
    if len(password1) < 8:
        raise ValidationError(
            'password is similar'
        )
    if password1 != password2:
        raise ValidationError(
            'passwords are not match'
        )
