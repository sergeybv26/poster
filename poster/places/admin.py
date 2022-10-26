from django.contrib import admin

from places.models import Place, PlaceImage


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('uid',)


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    exclude = ('uid',)
