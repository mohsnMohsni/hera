from .api import search, handle_cart, get_categories, get_shops
from django.urls import path
from .views import HomeView

app_name = 'siteview'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', search, name='search'),
    path('cart/', handle_cart, name='handle_cart'),
    path('header-menu/shop/', get_shops, name='get_shops'),
    path('header-menu/category/', get_categories, name='get_categories')
]
