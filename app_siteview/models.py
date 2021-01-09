from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from datetime import datetime
from pytz import utc


class SlideShowImage(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    description = models.TextField(_('Description'))
    action_text = models.CharField(_('Action Text'), max_length=150)
    action_url = models.URLField(_('Action Url'))
    image = models.ImageField(_('Background'), upload_to='slideShowPictures/')

    class Meta:
        verbose_name = _('Slide Images')
        verbose_name_plural = _('Slide Images')

    def __str__(self):
        return self.title

    def slide_image(self):
        """ Return a html tag that have an image tag. """
        return format_html(
            f'<img src="{self.image.url}" width=80 height=50 "/>'
        )


# Custom Manager For OfferCards
class OfferManager(models.Manager):
    def is_confirm(self):
        return super().get_queryset().filter(show=True)


class OfferCards(models.Model):
    description = models.CharField(_('Description'), max_length=200)
    end_time = models.DateTimeField(_('End At'))
    image = models.ImageField(_('Offer Background'))
    show = models.BooleanField(_('Show Status'))
    update_at = models.DateTimeField(_('Update At'), auto_now=True)

    objects = OfferManager()

    class Meta:
        verbose_name = _('Offer Card')
        verbose_name_plural = _('Offer Cards')

    def __str__(self):
        """ Return show status """
        return 'show: ' + str(self.show)

    def save(self, *args, **kwargs):
        """
        If show status wants be update, check how many show status there is
        then if there is more than 2, update they status to false except last one.
        """
        if self.show is True:
            show_cards = OfferCards.objects.filter(show=True).order_by('update_at')
            if show_cards.count() >= 2:
                last_card = show_cards.first().end_time
                show_cards.filter(end_time__lt=last_card).update(show=False)
        return super(OfferCards, self).save(*args, **kwargs)

    def offer_background(self):
        """ Return a html tag that have an image tag. """
        return format_html(
            f'<img src="{self.image.url}" width=80 height=50 "/>'
        )

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
