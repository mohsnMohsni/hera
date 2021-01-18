from django.views.generic import TemplateView
from .models import SlideShowImage, OfferCards
from app_product.models import Shop, Category


class HomeView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slide_images'] = SlideShowImage.objects.all()
        context['best_shops'] = Shop.objects.order_by('shop_product')
        context['offer_cards'] = OfferCards.objects.is_confirm()
        context['category_list'] = Category.objects.filter(parent=None)
        q = context['category_list']
        print(q.first().get_children)
        return context


class SearchView(TemplateView):
    template_name = 'main/search.html'
