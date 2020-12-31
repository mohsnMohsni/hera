from django.contrib import admin
from .models import User, Email, Address
from django.contrib.auth.admin import UserAdmin as UserBaseAdmin
from django.utils.translation import ugettext_lazy as _


class EmailAdmin(admin.TabularInline):
    model = Email
    verbose_name = _('Email')
    verbose_name_plural = _('Emails')
    readonly_fields = ('subject', 'to', 'body')
    extra = 0


class AddressAdmin(admin.TabularInline):
    model = Address
    verbose_name = _('Address')
    verbose_name_plural = _('Addresses')
    readonly_fields = ('city', 'postal_code', 'street', 'alley', 'no')
    extra = 0


@admin.register(User)
class UserAdmin(UserBaseAdmin):
    list_display = ('email', 'is_staff', 'is_active')
    ordering = ('email',)
    add_fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password1', 'password2')}),
    )
    fieldsets = (
        (None, {'fields': ('email', 'full_name', 'password')}),
        ('Personal Option', {'fields': ('avatar',)}),
        ('Status', {'fields': ('is_staff', 'is_active', 'groups')})
    )
    inlines = (
        EmailAdmin,
        AddressAdmin,
    )
