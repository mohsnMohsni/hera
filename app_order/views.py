from .models import Basket
from django.views.generic import DetailView


class BasketDetail(DetailView):
    model = Basket
    template_name = 'order/basket.html'
    context_object_name = 'basket'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get()

    def get_queryset(self):
        query = Basket.objects.filter(user=self.request.user)
        if query.exists():
            return query
        else:
            query = Basket.objects.create(user=self.request.user)
            return query
