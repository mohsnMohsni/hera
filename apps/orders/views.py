from .models import Cart, Order, OrderItem, OrderMeta
from django.views.generic import DetailView
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class CartDetail(LoginRequiredMixin, DetailView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'order/cart.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


def submit_order(request):
    if request.method == 'POST':
        cart_items = request.user.cart.cart_item.all_unique()
        description = request.POST.get('description')
        order = Order.objects.create(cart=request.user.cart, description=description)
        cart_meta = request.user.cart.cart_meta.all()
        for _ in cart_meta:
            OrderMeta.objects.create(order=order, shop_product=_.shop_product,
                                     label=_.label, value=_.value)
        for cart_item in cart_items:
            OrderItem.objects.create(order=order, shop_product=cart_item.shop_product,
                                     price=cart_item.shop_product.price,
                                     count=cart_item.count_same.count())
        cart_meta.delete()
        request.user.cart.cart_item.all().delete()
        return redirect('account:user_profile')
    return HttpResponse('Bad Request', status=400)
