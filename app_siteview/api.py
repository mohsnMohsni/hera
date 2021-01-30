from .serializers import ProductSearchSerializer, CategorySearchSerializer
from app_product.models import Product, Category, ShopProduct
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from app_order.models import CartItem
from django.db.models import Q


@csrf_exempt
def search(request):
    """
    Get value from request.GET and filter products, categories with Q objects.
    Q objects can help us to use complex filter.
    then user serializer for serializer the data and return a json.
    If values is empty return empty list.
    """
    if request.method == 'POST':
        product_value = request.POST.get('product_value', '')
        if product_value != "":
            products = Product.objects.filter(
                Q(name__icontains=product_value) | Q(category__name__icontains=product_value) |
                Q(detail__icontains=product_value) | Q(brand__name__contains=product_value)
            )
        else:
            products = []
        products = ProductSearchSerializer(products, many=True)
        category_value = request.POST.get('category_value', '')
        if category_value != "":
            categories = Category.objects.filter(
                Q(name__icontains=category_value) | Q(slug__icontains=category_value) |
                Q(detail__icontains=category_value) | Q(product__name__contains=category_value)
            )
        else:
            categories = []
        categories = CategorySearchSerializer(categories, many=True)
        return JsonResponse({'products': products.data, 'categories': categories.data}, safe=False)
    else:
        return HttpResponse('Allow method: POST', 400)


@csrf_exempt
def handle_cart(request):
    if request.method == 'GET':
        count = request.user.cart.products_count
        return JsonResponse({'product_count': count}, safe=False)
    else:
        pk = request.POST.get('id', None)
        shop_product = ShopProduct.objects.filter(pk=pk).first() or None
        if shop_product is not None:
            CartItem.objects.create(shop_product=shop_product, cart=request.user.cart)
        return HttpResponse(status=201)
