from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('User'),
                                related_name='cart', related_query_name='cart')

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return str(self.user)

    @property
    def products_count(self):
        """
        Count products there is in cart.
        """
        return self.cart_item.all().count()

    @property
    def total_price(self):
        """
        Return total price off all products add to this cart
        and that's related to User have been send request.
        """
        return Cart.objects.filter(user=self.user).aggregate(
            models.Sum('cart_item__shop_product__price')
        ).get('cart_item__shop_product__price__sum')


class CartItemManager(models.Manager):
    def all_unique(self):
        """
        Get all basket item and their shop_product's id,
        then if shop_product.id exists in list return it and pop it's id from shop_product.id list
        """
        all_query = self.get_queryset()
        shop_product_id = list(set(all_query.values_list('shop_product', flat=True)))
        unique_list = list()
        for item in all_query:
            if item.shop_product.id in shop_product_id:
                unique_list.append(item)
                i = shop_product_id.index(item.shop_product.id)
                shop_product_id.pop(i)
        return unique_list


class CartItem(models.Model):
    cart = models.ForeignKey("Cart", verbose_name=_('Cart'), on_delete=models.CASCADE,
                             related_name='cart_item', related_query_name='cart_item')
    shop_product = models.ForeignKey('app_product.ShopProduct', verbose_name=_('Shop Product'),
                                     on_delete=models.CASCADE,
                                     related_name='cart_item', related_query_name='cart_item')

    objects = CartItemManager()

    class Meta:
        verbose_name = _('Cart Item')
        verbose_name_plural = _('Cart Items')

    def __str__(self):
        return str(self.cart)

    @property
    def count_same(self):
        """
        Return quantity of this item, which there is in the cart
        that's related to user have been send request.
        """
        return CartItem.objects.filter(
            shop_product=self.shop_product, cart__user=self.cart.user
        )

    @property
    def same_product_id(self):
        """
        Return same product's id
        """
        return list(self.count_same.values_list('id', flat=True))


class Order(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE, verbose_name=_('Cart'),
                             related_name='order', related_query_name='order')
    create_at = models.DateTimeField(_('Create At'), auto_now_add=True)
    description = models.CharField(_('Description'), max_length=150)

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    def __str__(self):
        return str(self.cart)

    @property
    def total_price(self):
        """
        Return total price off all products add to this cart
        and that's related to User have been send request.
        """
        query_object = Order.objects.get(cart=self.cart, create_at=self.create_at).order_item.all()
        price_sum = 0
        for item in query_object:
            price_sum += item.item_price
        return price_sum


class OrderItem(models.Model):
    order = models.ForeignKey("Order", verbose_name=_('Order'), on_delete=models.CASCADE,
                              related_name='order_item', related_query_name='order_item')
    shop_product = models.ForeignKey('app_product.ShopProduct', verbose_name=_('Shop Product'),
                                     on_delete=models.CASCADE,
                                     related_name='order_item', related_query_name='order_item')
    count = models.IntegerField(_('Count'))
    price = models.IntegerField(_('Price'))

    class Meta:
        verbose_name = _('Order Item')
        verbose_name_plural = _('Order Items')

    def __str__(self):
        return str(self.order)

    @property
    def item_price(self):
        return self.price * self.count


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='payment', related_query_name='payment')
    order = models.OneToOneField("Order", on_delete=models.CASCADE, verbose_name=_('Order'),
                                 related_name='payment', related_query_name='payment')
    amount = models.IntegerField(_('Amount'))

    class Meta:
        verbose_name = _('Payment')
        verbose_name_plural = _('Payment')

    def __str__(self):
        return str(self.user)
