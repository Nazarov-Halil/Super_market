from django.db import models

from django.contrib.auth import get_user_model
from apps.products.models import Product

User = get_user_model()


class Cart(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f"{self.user}"

    def get_total_sum(self):
        return sum(i.get_subtotal_sum() for i in self.items_cart .all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Item(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='cart_item',
        verbose_name='Продукт'
    )
    quantity = models.PositiveSmallIntegerField(
        default=1,
        verbose_name='Каличество'
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='items_cart',
        verbose_name='Карзина',

    )

    def get_subtotal_sum(self):
        return int(self.quantity * self.product.price)

    def __str__(self):
        return f'{self.product.title}'


    class Meta:
        verbose_name = 'Элемент Корзина'
        verbose_name_plural = 'Элементы Корзины'
