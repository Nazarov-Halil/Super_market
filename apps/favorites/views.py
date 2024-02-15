from django.urls import reverse_lazy
from django.views import generic
from apps.favorites.models import Favorite, Item
from django.shortcuts import redirect
from apps.products.models import Product


class FavoriteDetailView(generic.ListView):
    template_name = 'favorite-detail.html'
    context_object_name = 'favorite'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['palto_product'] = Product.objects.filter(category__title='Пальто')[:4]
        context['trousers_product'] = Product.objects.filter(category__title='Штаны')[:4]
        context['sneakers_product'] = Product.objects.filter(category__title='Кроссы')[:4]

        return context

    def get_queryset(self):
        return Favorite.objects.get(user=self.request.user)
