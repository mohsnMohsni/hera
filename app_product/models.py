from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.utils.html import format_html
from image_cropping import ImageRatioField
from PIL import Image

User = get_user_model()


class AbstractDetail(models.Model):
    slug = models.SlugField(_('Slug'))
    name = models.CharField(_('Name'), max_length=150)
    detail = models.TextField(_('Detail'))
    cropping = ImageRatioField('image', '430x360', size_warning=True)
    image = models.ImageField(_('Image'))
    create_at = models.DateTimeField(_('Create Date'), auto_now_add=True)
    update_at = models.DateTimeField(_('Update Date'), auto_now=True)

    class Meta:
        abstract = True

    def _crop_image(self):
        """
        Get cropping value then initial space from top, left, right, bottom,
        and open file from path, crop it then resize it and at the end save it.
        """
        cropping_list = self.cropping.split(',')
        cropping_list = list(map(int, cropping_list))
        left, right = cropping_list[0], cropping_list[1]
        top, bottom = cropping_list[2], cropping_list[3]
        image = Image.open(self.image.path)
        cropped_image = image.crop((left, right, top, bottom))
        resized_image = cropped_image.resize((200, 200), Image.ANTIALIAS)
        return resized_image.save(self.image.path)


class Product(AbstractDetail):
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE, verbose_name=_('Brand'),
                              related_name='product', related_query_name='product')
    category = models.ForeignKey("Category", on_delete=models.CASCADE, verbose_name=_('Category'),
                                 related_name='product', related_query_name='product')
    image = models.ImageField(_('Image'), upload_to='product/images', blank=True, null=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        abstract = False

    def __str__(self):
        return self.name

    def picture(self):
        """ Return a html tag that have an image tag. """
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width=60 height=50 style="border-radius:5px"/>'
            )
        else:
            return '---'

    def save(self, *args, **kwargs):
        """
        Check if cropping there is, calling crop_image()
        """
        if Product.objects.filter(image=self.image).exists():
            self._crop_image()
        return super(Product, self).save(*args, **kwargs)


class ProductMeta(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='meta_field', related_query_name='meta_field')
    label = models.CharField(_('Label'), max_length=100)
    value = models.CharField(_('Value'), max_length=100)

    class Meta:
        verbose_name = _('Product Meta Data')
        verbose_name_plural = _('Product Meta Detail')

    def __str__(self):
        return str(self.product) + f'({self.label})'


class Brand(AbstractDetail):
    slug = None
    image = models.ImageField(_('Image'), upload_to='brand/images', blank=True)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.name

    def picture(self):
        """ Return a html tag that have an image tag. """
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width=60 height=50 style="border-radius:50%"/>'
            )
        else:
            return '---'

    def save(self, *args, **kwargs):
        """
        Check if cropping there is, calling crop_image()
        """
        if Brand.objects.filter(image=self.image).exists():
            self._crop_image()
        return super(Brand, self).save(*args, **kwargs)


class Category(AbstractDetail):
    parent = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name=_('Parent'),
                               blank=True, null=True,
                               related_name='children', related_query_name='children')
    image = models.ImageField(_('Image'), upload_to='category/images', blank=True)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name

    def picture(self):
        """ Return a html tag that have an image tag. """
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width=60 height=50 style="border-radius:50%"/>'
            )
        else:
            return '---'

    def save(self, *args, **kwargs):
        """
        Check if cropping there is, calling crop_image()
        """
        if Category.objects.filter(image=self.image).exists():
            self._crop_image()
        return super(Category, self).save(*args, **kwargs)


class Gallery(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='images', related_query_name='images')
    image = models.ImageField(_('Image'), upload_to='product/GalleryImage')

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Gallery')

    def __str__(self):
        return str(self.product)

    def picture(self):
        """ Return a html tag that have an image tag. """
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width=60 height=50 style="border-radius:50%"/>'
            )
        else:
            return '---'


class Shop(AbstractDetail):
    image = models.ImageField(_('Picture'), upload_to='shop/images', blank=True)

    class Meta:
        verbose_name = _('Shop')
        verbose_name_plural = _('Shops')

    def __str__(self):
        return self.name

    def picture(self):
        """
        Return a html tag that have an image tag.
        """
        if self.image:
            return format_html(
                f'<img src="{self.image.url}" width=60 height=50 style="border-radius:50%"/>'
            )
        else:
            return '---'

    def save(self, *args, **kwargs):
        """
        Check if cropping there is, calling crop_image()
        """
        if Shop.objects.filter(image=self.image).exists():
            self._crop_image()
        return super(Shop, self).save(*args, **kwargs)


class ShopProduct(models.Model):
    shop = models.ForeignKey("Shop", on_delete=models.CASCADE, verbose_name=_('Shop'),
                             related_name='shop_product', related_query_name='shop_product')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_('Product'),
                                related_name='shop_product', related_query_name='shop_product')
    price = models.IntegerField(_('Price'))
    quantity = models.IntegerField(_('Quantity'))

    class Meta:
        verbose_name = _('Shop Product')
        verbose_name_plural = _('Shop Products')

    def __str__(self):
        return f'{str(self.shop)}-{str(self.product)}'


class Comment(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name=_('Product'),
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


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('User'),
                             related_name='likes', related_query_name='likes')
    products = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name=_('Products liked'),
                                 related_name='likes', related_query_name='likes')
    condition = models.BooleanField(_('Condition'), blank=True)

    class Meta:
        verbose_name = _('Like')
        unique_together = [('user', 'condition')]

    def __str__(self):
        return str(self.user)
