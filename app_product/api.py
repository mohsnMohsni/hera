from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.db.models import Q
from rest_framework.response import Response
from .models import Product, Category
from .serializers import CategorySerializer, ProductSerializer


class CategoryAPI(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductAPI(RetrieveAPIView):
    queryset = Product.objects.all()
    lookup_field = 'slug'
    serializer_class = ProductSerializer


class SearchAPI(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(name__contains=query) | Q(slug__contains=query)
        )
        return object_list

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            serializer_data = serializer.data
            serializer_data.append({'search_key': self.request.GET.get('search')})
            return self.get_paginated_response(serializer_data)

        serializer = self.get_serializer(queryset, many=True)
        serializer_data = serializer.data
        serializer_data.append({'search_key': self.request.GET.get('search')})
        return Response(serializer_data)
