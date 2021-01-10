from django.views.generic import DetailView
from .models import Category, Product


class CategoryDetail(DetailView):
    model = Category
    template_name = 'main/category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        products = Product.objects.prefetch_related('shop_product').filter(category=context.get('category'))[:8]
        context['products'] = products
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'main/product.html'
