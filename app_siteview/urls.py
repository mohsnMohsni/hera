from django.urls import path
from .views import HomeView, SearchView

app_name = 'siteview'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search')
]
