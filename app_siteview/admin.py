from django.contrib import admin
from .models import SlideShowImage
from image_cropping import ImageCroppingMixin


@admin.register(SlideShowImage)
class SlideShowAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'picture', 'have_time')
