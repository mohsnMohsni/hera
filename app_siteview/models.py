from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html
from image_cropping import ImageRatioField
from PIL import Image
from datetime import datetime
from pytz import utc


class SlideShowImage(models.Model):
    action_text = models.CharField(_('Action Text'), max_length=35)
    action_url = models.URLField(_('Action Url'))
    description = models.CharField(_('Description'), max_length=150)
    crop_it = models.BooleanField(_('Crop It'), default=False)
    title = models.CharField(_('Title'), max_length=100)
    image = models.ImageField(_('Background'), upload_to='slideShowPictures/images')
    cropping = ImageRatioField('image', '530x360', size_warning=True)
    end_time = models.DateTimeField(_('End At'))

    class Meta:
        verbose_name = _('Slide Show')
        verbose_name_plural = _('Slide Shows')

    def __str__(self):
        return self.title

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

    def picture(self):
        """ Return a html tag that have an image tag. """
        return format_html(
            f'<img src="{self.image.url}" width=80 height=50 "/>'
        )

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

    def save(self, *args, **kwargs):
        """
        Colling show_status() and check if cropping there is, calling crop_image()
        """
        if SlideShowImage.objects.filter(image=self.image).exists() and self.crop_it is True:
            self._crop_image()
            self.crop_it = False
        return super(SlideShowImage, self).save(*args, **kwargs)
