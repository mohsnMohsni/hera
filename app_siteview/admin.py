from django.contrib import admin
from .models import SlideShowImage, OfferCards


@admin.register(SlideShowImage)
class SlideShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'slide_image')


@admin.register(OfferCards)
class OfferCardsAdmin(admin.ModelAdmin):
    list_display = ('offer_background', 'description', 'have_time', 'show')
    list_display_links = ('offer_background', 'description')
