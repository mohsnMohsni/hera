from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

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


class ProductMeta(models.Model):
    product = models.ForeignKey(_('Product'), on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='meta_field', related_query_name='meta_field')
    label = models.CharField(_('Label'), max_length=100)
    value = models.CharField(_('Value'), max_length=100)


class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    detail = models.TextField(_('Detail'))
    image = models.ImageField(_('Image'), upload_to='brand/images', blank=True)


class Category(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name=_('Parent'),
                               related_name='children', related_query_name='children')
    name = models.CharField(_('Name'), max_length=100)
    slug = models.SlugField(_('Slug'))
    detail = models.TextField(_('Detail'))
    image = models.ImageField(_('Image'), upload_to='category/images', blank=True)


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='images', related_query_name='images')
    image = models.ImageField(_('Image'), upload_to='product/GalleryImage')


class Off(models.Model):
    product = models.ManyToManyField(Product, verbose_name=_('Product'),
                                     related_name='product', related_query_name='product')
    description = models.CharField(_('Description'), max_length=150)
    percent = models.IntegerField(_('Percent'))


class ShopProduct(models.Model):
    shop = models.ForeignKey('Shop', on_delete=models.CASCADE, verbose_name=_('Shop'),
                             related_name='shop_product', related_query_name='shop_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='shop_product', related_query_name='shop_product')
    price = models.IntegerField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))


class Comments(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='comments', related_query_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='comments', related_query_name='comments')
    text = models.TextField(_('Text'))
    rate = models.IntegerField(_('Rate'))
