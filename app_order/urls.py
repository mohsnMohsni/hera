from .views import CartDetail, submit_order
from django.urls import path
from .api import delete_item

app_name = 'order'

urlpatterns = [
    path('cart/', CartDetail.as_view(), name='cart'),
    path('delete_item/', delete_item, name='delete_item'),
    path('submit_order/', submit_order, name='submit_order')
]
