from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class AppSiteviewConfig(AppConfig):
    name = 'app_siteview'
    verbose_name = _('siteview')
