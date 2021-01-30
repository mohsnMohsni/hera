from .views import CartDetail
from django.urls import path
from .api import delete_item

app_name = 'order'

urlpatterns = [
    path('cart/', CartDetail.as_view(), name='cart'),
    path('delete_item/', delete_item, name='delete_item')
]
