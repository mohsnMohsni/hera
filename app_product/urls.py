from django.urls import path
from .views import CategoryList

app_name = 'product'

urlpatterns = [
    path('category/<slug:slug>/', CategoryList.as_view(), name='category'),
]
