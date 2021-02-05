from django.views.generic import TemplateView, RedirectView
from app_product.models import Category
from django.shortcuts import reverse
from .models import SlideShowImage


class ChangeDefaultLanguage(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('siteview:home')[:1] + 'fa/'


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = SlideShowImage.objects.all()
        context['categories'] = Category.objects.filter(parent=None)
        return context
