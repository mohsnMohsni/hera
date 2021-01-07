from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.html import format_html


class SlideShowImage(models.Model):
    title = models.CharField(_('Title'), max_length=150)
    description = models.TextField(_('Description'))
    action_text = models.CharField(_('Action Text'), max_length=150)
    action_url = models.URLField(_('Action Url'))
    image = models.ImageField(_('Image'), upload_to='slideShowPictures/')

    class Meta:
        verbose_name = _('Slide Images')
        verbose_name_plural = _('Slide Images')

    def __str__(self):
        return self.title

    def slide_image(self):
        return format_html(
            f'<img src="{self.image.url}" width=80 height=50 "/>'
        )
