from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppProductConfig(AppConfig):
    name = 'app_product'
    verbose_name = _('product')
