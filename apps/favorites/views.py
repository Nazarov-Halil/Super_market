from django.shortcuts import redirect
from django.views import generic
from apps.favorites.models import Favorite, Item
from apps.products.models import Product

class FavoriteDetailView(generic.ListView):
    template_name = 'favorite-detail.html'
    context_object_name = 'favorite'

    def get_queryset(self):
        return Favorite.objects.get(user=self.request.user)

def add_to_favorite(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        favorite, created = Favorite.objects.get_or_create(user=request.user)
        if created:
            favorite.save()
        Item.objects.create(product=product, favorite=favorite)
    return redirect('favorite')
