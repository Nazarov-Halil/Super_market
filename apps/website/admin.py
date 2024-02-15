from django.contrib import admin
from apps.website.models import Slider, WebSiteSettings


class SliderInline(admin.TabularInline):
    model = WebSiteSettings.slider.through
    extra = 3


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['image']


@admin.register(WebSiteSettings)
class WebSiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['title']
    exclude = ['slider']
    inlines = [SliderInline]
