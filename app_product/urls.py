from django.urls import path
from .views import CategoryDetail, ProductDetail, SearchView
from .api import add_comment

app_name = 'product'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
    path('search/', SearchView.as_view(), name='search'),
    path('add_comment/', add_comment, name='add_comment'),
]
