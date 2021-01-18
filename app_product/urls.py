from django.urls import path
from .views import CategoryDetail, ProductDetail, SearchView

app_name = 'product'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
    path('search/', SearchView.as_view(), name='search'),
]
