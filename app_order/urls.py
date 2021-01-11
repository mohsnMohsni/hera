from django.urls import path
from .views import BasketDetail

app_name = 'order'

urlpatterns = [
    path('basket/', BasketDetail.as_view(), name='basket'),
]
