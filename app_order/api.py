from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import CartMetaSerializers
from django.http import HttpResponse
from .models import CartItem
import json


@csrf_exempt
def add_cart_meta(request):
    if request.method == 'POST':
        shop_product_id = request.POST.getlist('id')[0]
        label = request.POST.getlist('label')[0]
        value = request.POST.getlist('value')[0]
        data = {'shop_product': shop_product_id, 'label': label, 'value': value, 'cart': request.user.cart.id}
        serializer = CartMetaSerializers(data=data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse('ok')
        return HttpResponse('NOT Valid', status=400)
    else:
        return HttpResponse('Allow Method: POST', status=400)


@csrf_exempt
def delete_item(request):
    if request.method == 'POST':
        pk = request.POST.get('pk', None)
        if pk:
            CartItem.objects.filter(pk=pk).delete()
            return HttpResponse(status=204)
        else:
            return HttpResponse('Pk Not available', status=404)
    else:
        return HttpResponse('Allow Method: POST', status=400)
