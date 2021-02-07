from .views import (ProductList, ProductDetail, ShopProductList, AddShopView, AddShopProductView,
                    EditShopProductView, EditShopView, add_product_image, product_meta)
from .api import add_comment, like_product
from django.urls import path

app_name = 'product'

urlpatterns = [  # View for show detail
                  path('<slug:slug>/', ShopProductList.as_view(), name='shop_product_list'),
                  path('category/<slug:slug>/', ProductList.as_view(), name='category'),
                  path('product/<slug:slug>/<int:shop_product_id>/', ProductDetail.as_view(), name='product'),
              ] + [  # Api handle path's
                  path('api/add_comment/', add_comment, name='add_comment'),
                  path('api/like_product/', like_product, name='like_product'),
              ] + [  # Form handle path's
                  path('add/new_shop/', AddShopView.as_view(), name='add_shop'),
                  path('add/new_product/', AddShopProductView.as_view(), name='add_product'),
                  path('add/gallery_product/<slug:slug>/<int:shop_product_id>/', add_product_image,
                       name='add_product_image'),
                  path('add/add_product_meta/<slug:slug>/<int:shop_product_id>/', product_meta, name='product_meta'),

                  path('edit/product/<slug:slug>/<int:shop_product_id>/', EditShopProductView.as_view(),
                       name='edit_product'),
                  path('edit/shop/<slug:slug>/', EditShopView.as_view(), name='edit_shop'),
              ]
