from django.urls import path
from .views import CartDetail

app_name = 'order'

urlpatterns = [
    path('cart/', CartDetail.as_view(), name='cart'),
]
