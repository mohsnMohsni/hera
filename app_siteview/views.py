from django.views.generic import TemplateView
from .models import SlideShowImage, OfferCards
from app_product.models import Shop


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slide_images'] = SlideShowImage.objects.all()
        context['best_shops'] = Shop.objects.all()[:3]
        context['offer_cards'] = OfferCards.objects.is_confirm()
        return context
