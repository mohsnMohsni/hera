from django.urls import path
from .views import HomeView
from .api import search

app_name = 'siteview'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', search, name='search')
]
