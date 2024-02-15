from django.urls import path
from apps.favorites.views import FavoriteDetailView

urlpatterns = [
    path('favorite/', FavoriteDetailView.as_view(), name='favorite')
]
