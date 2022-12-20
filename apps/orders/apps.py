from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppOrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.orders'
    verbose_name = _('order')
