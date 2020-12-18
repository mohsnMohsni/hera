from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from app_product.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='cart', related_query_name='cart')
    is_active = models.BooleanField(_('Active status'))
    send_time = models.DateTimeField(_('Send time'))

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return str(self.user)


class Order(models.Model):
    products = models.ManyToManyField(Product, verbose_name=_('Products'),
                                      related_name='order', related_query_name='order')
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, verbose_name=_('Cart'),
                             related_name='order', related_query_name='order')
    is_pass = models.BooleanField(_('Pass status'), blank=True, null=True)
    is_during = models.BooleanField(_('During status'), blank=True, null=True)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.cart)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='payment', related_query_name='payment')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=_('Order'),
                                 related_name='payment', related_query_name='payment')
    total_price = models.IntegerField(_('Total price'))
    pay_date = models.DateTimeField(_('Pay date'), auto_now_add=True)

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payment')

    def __str__(self):
        return str(self.user)
