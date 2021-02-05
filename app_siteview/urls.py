from .api import search, handle_cart
from django.urls import path
from .views import HomeView

app_name = 'siteview'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', search, name='search'),
    path('cart/', handle_cart, name='handle_cart'),
]
