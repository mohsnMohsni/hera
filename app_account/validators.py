from django.forms import ValidationError


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
