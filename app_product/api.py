from .serializers import CommentSerializer, LikeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser
from .models import Product, Like

User = get_user_model()


@csrf_exempt
def add_comment(request):
    """
    Check method is post and if it is true,
    get data from request.body and serialize it then check it is valid,
    at the end save comment and return status=201
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
    return HttpResponse('Bad Request', status=400)


@csrf_exempt
def like_product(request):
    """
    Check method is post and if it is true,
    get data from request.body then get product and user,
    if user like it change the current status if not create new and
    set status True.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        product = Product.objects.get(id=data.get('product'))
        user = User.objects.get(id=data.get('user'))
        try:
            like_object = Like.objects.get(user=user, products=product)
            status = not like_object.condition
            like_object.condition = status
            like_object.save()
        except Like.DoesNotExist:
            like_object = Like.objects.create(user=user, products=product, condition=True)
        return HttpResponse(f'{like_object.condition}', status=201)
    return HttpResponse('Bad Request', status=400)
