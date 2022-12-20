from .serializers import ProductSearchSerializer, CategorySearchSerializer, ShopSerializer
from apps.products.models import Product, Category, ShopProduct, Shop
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from apps.orders.models import CartItem
from django.db.models import Q
import redis


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
    """
    Using redis for caching cart data and if user is authenticated sort data in database
    """
    redis_server = redis.Redis('37.152.186.205')
    if request.user.is_authenticated:
        while redis_server.llen(f'{request.user.ip_address}') != 0:
            pk = redis_server.lpop(f'{request.user.ip_address}')
            shop_product = ShopProduct.objects.filter(pk=int(pk)).first() or None
            if shop_product is not None:
                CartItem.objects.create(shop_product=shop_product, cart=request.user.cart)

        if request.method == 'GET':
            count = request.user.cart.products_count
            return JsonResponse({'product_count': count}, safe=False)

        else:
            pk = request.POST.get('id', None)
            shop_product = ShopProduct.objects.filter(pk=pk).first() or None
            if shop_product is not None:
                CartItem.objects.create(shop_product=shop_product, cart=request.user.cart)
            return HttpResponse(status=201)
    else:
        if request.method == 'GET':
            if redis_server.exists(f'{request.user.ip_address}'):
                count = redis_server.llen(f'{request.user.ip_address}')
            else:
                count = 0
            return JsonResponse({'product_count': count}, safe=False)

        else:
            redis_server.rpush(f'{request.user.ip_address}', request.POST.get('id'))
            return HttpResponse(status=201)


def get_shops(request):
    shops = Shop.objects.all()
    shops = ShopSerializer(shops, many=True)
    return JsonResponse({'shops': shops.data}, safe=False)


def get_categories(request):
    categories = Category.objects.filter(parent=None)
    categories = CategorySearchSerializer(categories, many=True)
    return JsonResponse({'categories': categories.data}, safe=False)
