from django.urls import path
from .views import ProductList, ProductDetail
from .api import add_comment, like_product

app_name = 'product'

urlpatterns = [
    path('category/<slug:slug>/', ProductList.as_view(), name='category'),
    path('product/<slug:slug>/<int:shop_product_id>/', ProductDetail.as_view(), name='product'),
    path('add_comment/', add_comment, name='add_comment'),
    path('like_product/', like_product, name='like_product'),
]
