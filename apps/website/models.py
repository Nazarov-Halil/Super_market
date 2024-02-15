from django.db import models


class Slider(models.Model):
    image = models.ImageField(
        upload_to='slider/',
        verbose_name='Картинка'
    )


class WebSiteSettings(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    slider = models.ManyToManyField(
        Slider,
        blank=True,
        verbose_name='Слайдер'
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Настройка сайта'
        verbose_name_plural = 'Настройки сайта'
