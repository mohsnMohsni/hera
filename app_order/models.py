from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from app_product.models import Product

User = get_user_model()


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='basket', related_query_name='basket')
    send_time = models.DateTimeField(_('Send time'))

    class Meta:
        verbose_name = _('Basket')
        verbose_name_plural = _('Basket')

    def __str__(self):
        return str(self.user)


class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, verbose_name=_('Basket'), on_delete=models.CASCADE,
                               related_name='basket_item', related_query_name='basket_item')
    shop_product = models.ForeignKey('app_product.ShopProduct', verbose_name=_('Shop Product'), on_delete=models.CASCADE,
                                     related_name='basket_item', related_query_name='basket_item')

    class Meta:
        verbose_name = _('Basket Item')
        verbose_name_plural = _('Basket Items')

    def __str__(self):
        return str(self.basket)


class Order(models.Model):
    products = models.ManyToManyField(Product, verbose_name=_('Products'),
                                      related_name='order', related_query_name='order')
    cart = models.ForeignKey(Basket, on_delete=models.CASCADE, verbose_name=_('Cart'),
                             related_name='order', related_query_name='order')
    create_at = models.DateTimeField(_('Create At'), auto_now_add=True)
    update_at = models.DateTimeField(_('Update At'), auto_now=True)
    description = models.CharField(_('Description'), max_length=150)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.cart)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=_('Order'), on_delete=models.CASCADE,
                              related_name='order_item', related_query_name='order_item')
    shop_product = models.ForeignKey('app_product.ShopProduct', verbose_name=_('Shop Product'), on_delete=models.CASCADE,
                                     related_name='order_item', related_query_name='order_item')
    count = models.IntegerField(_('Count'))
    price = models.IntegerField(_('Price'))

    class Meta:
        verbose_name = _('Basket Item')
        verbose_name_plural = _('Basket Item')

    def __str__(self):
        return str(self.order)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='payment', related_query_name='payment')
    order = models.OneToOneField(Order, on_delete=models.CASCADE, verbose_name=_('Order'),
                                 related_name='payment', related_query_name='payment')
    amount = models.IntegerField(_('Amount'))

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payment')

    def __str__(self):
        return str(self.user)
