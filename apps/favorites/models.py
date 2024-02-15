from django.db import models
from django.contrib.auth import get_user_model

from apps.products.models import Product

User = get_user_model()


class Favorite(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='favorite',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранные'


class Item(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name='favorite_item',
        verbose_name='Продукт'
    )
    favorite = models.ForeignKey(
        Favorite, on_delete=models.CASCADE,
        related_name='items_favorites',
        verbose_name='Избранный'
    )

    def __str__(self):
        return f'{self.product.title}'

    class Meta:
        verbose_name = 'Элемент Избранный'
        verbose_name_plural = 'Элементы Избранных'
