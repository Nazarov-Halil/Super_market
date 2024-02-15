from django.contrib import admin
from apps.favorites.models import Favorite, Item
admin.site.register(Favorite)
admin.site.register(Item)