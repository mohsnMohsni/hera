from .models import Basket
from django.views.generic import DetailView, TemplateView


class BasketDetail(TemplateView):
    # model = Basket
    template_name = 'order/basket.html'
