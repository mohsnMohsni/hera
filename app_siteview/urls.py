from django.urls import path
from .views import HomeView
from .api import search, handle_cart
from django.conf.urls.i18n import i18n_patterns

app_name = 'siteview'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', search, name='search'),
    path('cart/', handle_cart, name='handle_cart'),
]

# urlpatterns += [
#     i18n_patterns(
#         path('', HomeView.as_view(), name='home'),
#         path('search/', search, name='search'),
#         path('cart/', handle_cart, name='handle_cart'),
#     )
# ]
