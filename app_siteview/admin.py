from django.contrib import admin
from .models import SlideShowImage


@admin.register(SlideShowImage)
class SlideShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'slide_image')


