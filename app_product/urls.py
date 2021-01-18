from django.urls import path
from .views import CategoryDetail, ProductDetail, SearchView
from .api import CategoryAPI, ProductAPI, SearchAPI


app_name = 'product'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category'),
    # path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
    path('search1/', SearchView.as_view(), name='search'),
    path('category/', CategoryAPI.as_view()),
    path('product/<slug:slug>/', ProductAPI.as_view()),
    path('search/', SearchAPI.as_view()),
]
