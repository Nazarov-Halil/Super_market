from django.views import generic
from apps.cart.models import Cart, Item
from django.shortcuts import redirect


class CartDetailView(generic.ListView):
    template_name = 'cart-detail.html'
    context_object_name = 'cart'

    def get_queryset(self):
        return Cart.objects.get(user=self.request.user)


class QuantityChangeLogics:
    @staticmethod
    def minus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        if item.quantity - 1 == 0:
            item.delete()
            return redirect('cart')
        item.quantity -= 1
        item.save()
        return redirect('cart')

    @staticmethod
    def pilus_quantity(request, pk):
        item = Item.objects.get(id=pk)
        item.quantity += 1
        item.save()
        return redirect('cart')
