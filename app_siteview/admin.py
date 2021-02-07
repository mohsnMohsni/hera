from django.contrib import admin
from .models import SlideShowImage
from image_cropping import ImageCroppingMixin


@admin.register(SlideShowImage)
class SlideShowAdmin(ImageCroppingMixin, admin.ModelAdmin):
    """
    SlideShowImage admin, which to use for mange SlideShowImage data,
    and inherited from ImageCroppingMixin to add crop image Feature
    """
    list_display = ('action_text', 'picture', 'have_time')
