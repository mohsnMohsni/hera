from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from app_account.models import Shop

User = get_user_model()


class Product(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name=_('Brand'),
                              related_name='brand', related_query_name='brand')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_('Category'),
                                 related_name='category', related_query_name='category')
    slug = models.SlugField(_('Slug'))
    name = models.CharField(_('Name'), max_length=150)
    image = models.ImageField(_('Image'), upload_to='product/images', blank=True, null=True)
    detail = models.TextField(_('Detail'))

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self):
        return self.name


class ProductMeta(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='meta_field', related_query_name='meta_field')
    label = models.CharField(_('Label'), max_length=100)
    value = models.CharField(_('Value'), max_length=100)

    class Meta:
        verbose_name = _('Product Meta Data')
        verbose_name_plural = _('Product Meta Detail')

    def __str__(self):
        return str(self.product) + f'({self.label})'


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    detail = models.TextField(_('Detail'))
    image = models.ImageField(_('Image'), upload_to='brand/images', blank=True)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name=_('Parent'),
                               related_name='children', related_query_name='children')
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'))
    detail = models.TextField(_('Detail'))
    image = models.ImageField(_('Image'), upload_to='category/images', blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='images', related_query_name='images')
    image = models.ImageField(_('Image'), upload_to='product/GalleryImage')

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')

    def __str__(self):
        return str(self.product)


class Off(models.Model):
    product = models.ManyToManyField(Product, verbose_name=_('Product'),
                                     related_name='product', related_query_name='product')
    description = models.CharField(_('Description'), max_length=150)
    percent = models.IntegerField(_('Percent'))

    class Meta:
        verbose_name = _('Off')
        verbose_name_plural = _('Offs')

    def __str__(self):
        return self.description


class ShopProduct(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, verbose_name=_('Shop'),
                             related_name='product_shop', related_query_name='product_shop')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='shop_product', related_query_name='shop_product')
    price = models.IntegerField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))

    class Meta:
        verbose_name = _('Shop Product')
        verbose_name_plural = _('Shop Products')

    def __str__(self):
        return f'{str(self.shop)}-{str(self.product)}'


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='comments', related_query_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='comments', related_query_name='comments')
    text = models.TextField(_('Text'))
    rate = models.IntegerField(_('Rate'))

    class Meta:
        verbose_name = _('Comments')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return str(self.user)
