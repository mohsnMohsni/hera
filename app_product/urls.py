from django.urls import path
from .views import CategoryDetail, ProductDetail, SearchView
from .api import add_comment, like_product

app_name = 'product'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
    path('search/', SearchView.as_view(), name='search'),
    path('add_comment/', add_comment, name='add_comment'),
    path('like_product/', like_product, name='like_product'),
]
