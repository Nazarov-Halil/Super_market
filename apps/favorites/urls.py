from django.urls import path
from apps.favorites.views import FavoriteDetailView, add_to_favorite

urlpatterns = [
    path('favorite/', FavoriteDetailView.as_view(), name='favorite'),
    path('add-to-favorite/<int:pk>/', add_to_favorite, name='add_to_favorite'),
]
