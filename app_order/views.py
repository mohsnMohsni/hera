from .models import Cart
from django.views.generic import DetailView


class CartDetail(DetailView):
    model = Cart
    template_name = 'order/basket.html'
    context_object_name = 'cart'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get()

    def get_queryset(self):
        """
        Return cart which is related to user have been send request,
        if it's is first time, and cart there is not,
        create a new cart for user.
        """
        query = Cart.objects.filter(user=self.request.user)
        if query.exists():
            return query
        else:
            query = Cart.objects.create(user=self.request.user)
            return query
