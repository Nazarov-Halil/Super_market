from django.shortcuts import render
from django.views import generic

from apps.categories.models import Category
from apps.products.models import Product
from apps.website.models import WebSiteSettings

class ProductListView(generic.ListView):
    model = Product
    template_name = 'base/../../templates/index.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['left_categories'] = Category.objects.filter(parent=None)
        context['palto_product'] = Product.objects.filter(category__title='Пальто')[:4]
        context['trousers_product'] = Product.objects.filter(category__title='Штаны')[:4]
        context['sneakers_product'] = Product.objects.filter(category__title='Кроссы')[:4]
        context['nav_categories'] = Category.objects.filter(parent=None)[:4]
        context['website'] = WebSiteSettings.objects.get(id=1)

        return context


class ProductDetailView(generic.DetailView):
    model = Product
    slug_field = 'slug'
    template_name = 'detail.html'


