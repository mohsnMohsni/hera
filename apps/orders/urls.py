from .views import CartDetail, submit_order
from .api import delete_item, add_cart_meta
from django.urls import path

app_name = 'order'

urlpatterns = [
    path('cart/', CartDetail.as_view(), name='cart'),
    path('cart_meta/', add_cart_meta, name='cart_meta'),
    path('delete_item/', delete_item, name='delete_item'),
    path('submit_order/', submit_order, name='submit_order')
]

