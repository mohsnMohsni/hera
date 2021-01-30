from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import CartItem, Cart


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
