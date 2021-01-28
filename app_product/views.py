from pprint import pprint
from django.views.generic import DetailView, ListView
from .models import Category, Product
from django.shortcuts import get_object_or_404


class CategoryDetail(ListView):
    model = Category
    paginate_by = 9
    slug_url_kwarg = 'slug'
    template_name = 'main/category.html'

    def get_queryset(self):
        """
        Get slug and then get category by slug, then get all products and return its.
        """
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
