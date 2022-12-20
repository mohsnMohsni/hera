from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from apps.siteviews.views import ChangeDefaultLanguage

urlpatterns = [
                  path('', ChangeDefaultLanguage.as_view())
              ] + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('apps.siteviews.urls')),
    path('shop/', include('apps.products.urls')),
    path('auth/', include('apps.accounts.urls')),
    path('order/', include('apps.orders.urls')),
)
