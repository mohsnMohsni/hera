from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.utils.html import format_html


class UserManager(BaseUserManager):
    def _create_user(self, email, full_name, password, **extra_fields):
        if not email:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, full_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, full_name, password, **extra_fields)

    def create_superuser(self, email, full_name=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, full_name, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'), db_index=True, unique=True,
                              help_text=_('required valid email like example@gamil.com'))
    full_name = models.CharField(_('Name'), max_length=100,
                                 help_text=_('enter your full name'))
    phone = models.IntegerField(_('Phone'), blank=True, default=0)
    avatar = models.ImageField(_('Avatar'), blank=True, upload_to='user/images')
    is_seller = models.BooleanField(_('User status'), blank=True, default=False)
    is_staff = models.BooleanField(_('Staff status'), default=False,
                                   help_text=_(
                                       'Designates whether the user can log into this admin site.'
                                   ))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_(
                                        'Designates whether this user should be treated as active.'
                                        'Unselect this instead of deleting accounts.'
                                    ))

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('full_name',)

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return str(self.email)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def profile_picture(self):
        if self.avatar:
            return format_html(
                f'<img src="{self.avatar.url}" width=60 height=50 style="border-radius:50%"/>'
            )
        else:
            return '---'


class Email(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='email_sent', related_query_name='email_sent')
    subject = models.CharField(_('Subject'), max_length=120)
    to = models.EmailField(_('To'))
    body = models.TextField(_('Text body'))

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    def __str__(self):
        return self.subject

    def get_email(self):
        return str(self.to)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='address', related_query_name='address')
    city = models.CharField(_('City'), max_length=100)
    street = models.CharField(_('Street'), max_length=100)
    alley = models.CharField(_('Alley'), max_length=50)
    no = models.IntegerField(_('Home no'))
    postal_code = models.IntegerField(_('Postal Code'))

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return self.city
