from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.products'
    verbose_name = _('product')
