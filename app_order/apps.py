from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppOrderConfig(AppConfig):
    name = 'app_order'
    verbose_name = _('order')
