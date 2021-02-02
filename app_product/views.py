from django.views.generic import DetailView, ListView, CreateView
from .models import Category, Product, ShopProduct, Shop
from django.shortcuts import get_object_or_404
from django.shortcuts import reverse
from .forms import AddShopForm


class ProductList(ListView):
    model = Product
    paginate_by = 12
    slug_url_kwarg = 'slug'
    template_name = 'main/category.html'

    def get_queryset(self):
        slug = self.kwargs.get(self.slug_url_kwarg)
        filter_value = self.request.GET.get('filter', 'Nothing')
        category = get_object_or_404(Category, slug=slug)
        self.kwargs['category'] = category
        return category.get_products(filter_value)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = self.kwargs.get('category')
        context['category'] = category
        context['children'] = category.get_children
        context['all_category'] = Category.objects.filter(parent=None)
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'main/product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        pk = self.kwargs.get('shop_product_id')
        context['shop_product'] = context['product'].shop_product.filter(pk=pk).first()
        return context


class ShopProductList(ListView):
    model = ShopProduct
    template_name = 'main/shop.html'
    paginate_by = 8

    def get_queryset(self):
        shop = get_object_or_404(Shop, slug=self.kwargs.get('slug'))
        self.kwargs['shop'] = shop
        return ShopProduct.objects.filter(shop=shop)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['shop'] = self.kwargs.get('shop')
        return context


class AddShopView(CreateView):
    model = Shop
    template_name = 'main/forms/add_shop.html'
    form_class = AddShopForm

    def form_valid(self, form):
        self.kwargs['slug'] = form.cleaned_data.get('slug')
        valid_form = form.save(commit=False)
        valid_form.user = self.request.user
        self.request.user.is_seller = True
        return super().form_valid(valid_form)

    def get_success_url(self):
        return reverse('product:shop_product_list', kwargs={'slug': self.kwargs.get('slug')})
