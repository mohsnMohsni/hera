from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from datetime import datetime
from pytz import utc
from image_cropping import ImageRatioField
from PIL import Image


class AbstractPanel(models.Model):
    image = models.ImageField(_('Abstract Image'))
    cropping = ImageRatioField('image', '430x360', size_warning=True)
    action_text = models.CharField(_('Action Text'), max_length=35)
    action_url = models.URLField(_('Action Url'))
    description = models.CharField(_('Description'), max_length=150)

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


class SlideShowImage(AbstractPanel):
    title = models.CharField(_('Title'), max_length=100)
    image = models.ImageField(_('Background'), upload_to='slideShowPictures/images')
    cropping = ImageRatioField('image', '530x360', size_warning=True)

    class Meta:
        verbose_name = _('Slide Images')
        verbose_name_plural = _('Slide Images')

    def __str__(self):
        return self.title

    def picture(self):
        """ Return a html tag that have an image tag. """
        return format_html(
            f'<img src="{self.image.url}" width=80 height=50 "/>'
        )

    def save(self, *args, **kwargs):
        """
        Colling show_status() and check if cropping there is, calling crop_image()
        """
        if SlideShowImage.objects.filter(image=self.image).exists():
            self._crop_image()
        return super(SlideShowImage, self).save(*args, **kwargs)


# Custom Manager For OfferCards
class OfferManager(models.Manager):
    def is_confirm(self):
        return super().get_queryset().filter(show=True)


class OfferCards(AbstractPanel):
    end_time = models.DateTimeField(_('End At'))
    show = models.BooleanField(_('Show Status'))
    update_at = models.DateTimeField(_('Update At'), auto_now=True)
    image = models.ImageField(_('Offer Background'), upload_to='offer-cards/images')
    cropping = ImageRatioField('image', '430x360', size_warning=True)

    objects = OfferManager()

    class Meta:
        verbose_name = _('Offer Card')
        verbose_name_plural = _('Offer Cards')

    def __str__(self):
        """ Return show status """
        return 'show: ' + str(self.show)

    def picture(self):
        """ Return a html tag that have an image tag. """
        return format_html(
            f'<img src="{self.image.url}" width=80 height=50 "/>'
        )

    def _show_status(self):
        """
        If show status wants be update, check how many show status there is
        then if there is more than 2, update they status to false except last one.
        """
        is_same = OfferCards.objects.filter(pk=self.pk, show=self.show).exists()
        if self.show is True and not is_same:
            show_cards = OfferCards.objects.filter(show=True).order_by('update_at')
            if show_cards.count() >= 2:
                last_card = show_cards.last().id
                show_cards.exclude(pk=int(last_card)).update(show=False)

    def save(self, *args, **kwargs):
        """
        Colling show_status() and check if cropping there is, calling crop_image()
        """
        self._show_status()
        if OfferCards.objects.filter(image=self.image).exists():
            self._crop_image()
        return super(OfferCards, self).save(*args, **kwargs)

    def _have_time(self):
        """
        Make localize datetime to compare with end time
        and check time have been finished or not.
        """
        if utc.localize(datetime.now()) <= self.end_time:
            return True
        return False

    _have_time.boolean = True
    have_time = _have_time
