from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppAccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.accounts'
    verbose_name = _('account')
