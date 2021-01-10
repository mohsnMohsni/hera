from django.urls import path
from .views import CategoryDetail, ProductDetail

app_name = 'product'

urlpatterns = [
    path('category/<slug:slug>/', CategoryDetail.as_view(), name='category'),
    path('product/<slug:slug>/', ProductDetail.as_view(), name='product'),
]
