from django.contrib import admin
from .models import SlideShowImage, OfferCards
from image_cropping import ImageCroppingMixin


@admin.register(SlideShowImage)
class SlideShowAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('title', 'picture')


@admin.register(OfferCards)
class OfferCardsAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ('picture', 'description', 'have_time', 'show')
    list_display_links = ('picture', 'description')
