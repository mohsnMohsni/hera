from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework.parsers import JSONParser
from .serializers import CommentSerializer
from django.http import JsonResponse, HttpResponse
from .models import Comment, Product

User = get_user_model()


@csrf_exempt
def add_comment(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False, status=201)
    return HttpResponse('Bad Request', status=400)
