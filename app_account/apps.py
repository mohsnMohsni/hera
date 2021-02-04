from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppAccountConfig(AppConfig):
    name = 'app_account'
    verbose_name = _('account')
