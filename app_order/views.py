from .models import Basket
from django.views.generic import ListView


class BasketDetail(ListView):
    model = Basket
    template_name = 'order/basket.html'

    def get_queryset(self):
        return Basket.objects.get(user=self.request.user)
