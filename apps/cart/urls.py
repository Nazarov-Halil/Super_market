from django.urls import path

from apps.cart.views import CartDetailView, QuantityChangeLogics

urlpatterns = [
    path('cart/', CartDetailView.as_view(), name='cart'),
    path('minus/<int:pk>/', QuantityChangeLogics.minus_quantity, name='minus_quantity'),
    path('pilus/<int:pk>/', QuantityChangeLogics.pilus_quantity, name='pilus_quantity')
]
