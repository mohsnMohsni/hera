from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppSiteviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.siteviews'
    verbose_name = _('siteview')
