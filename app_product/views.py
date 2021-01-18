from django.db.models import Q
from django.views.generic import DetailView, ListView
from .models import Category, Product


class CategoryDetail(DetailView):
    model = Category
    template_name = 'main/category.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        products = Product.objects.prefetch_related(
            'shop_product'
        ).filter(category=context.get('category'))[:8]
        context['products'] = products
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'main/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['product1'] = Product.objects.all().values_list('id', flat=True)
        print(context['product1'])
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
