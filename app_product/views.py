from pprint import pprint
from django.db.models import Q
from django.views.generic import DetailView, ListView
from .models import Category, Product
from django.shortcuts import get_object_or_404


class CategoryDetail(ListView):
    model = Category
    paginate_by = 9
    slug_url_kwarg = 'slug'
    template_name = 'main/category.html'

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        category = get_object_or_404(Category, slug=slug)
        self.kwargs['category'] = category
        return category.get_products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = self.kwargs.get('category')
        context['children'] = category.get_children
        context['category'] = category
        context['all_category'] = Category.objects.filter(parent=None)
        pprint(context)
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'main/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class SearchView(ListView):
    model = Product
    template_name = 'main/search.html'
    paginate_by = 8

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(name__contains=query) | Q(slug__contains=query)
        )
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['search_key'] = self.request.GET.get('search')
        return context
