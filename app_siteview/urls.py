from django.urls import path
from .views import HomeView, SearchView
from django.views.decorators.csrf import csrf_exempt

app_name = 'siteview'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search/', SearchView.as_view(), name='search')
]
