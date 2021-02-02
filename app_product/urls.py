from .views import ProductList, ProductDetail, ShopProductList, AddShopView, AddShopProductView
from .api import add_comment, like_product
from django.urls import path

app_name = 'product'

urlpatterns = [
    path('<slug:slug>/', ShopProductList.as_view(), name='shop_product_list'),
    path('category/<slug:slug>/', ProductList.as_view(), name='category'),
    path('product/<slug:slug>/<int:shop_product_id>/', ProductDetail.as_view(), name='product'),
    path('api/add_comment/', add_comment, name='add_comment'),
    path('api/like_product/', like_product, name='like_product'),
    path('add/new_shop/', AddShopView.as_view(), name='add_shop'),
    path('add/new_product/', AddShopProductView.as_view(), name='add_product'),
]
