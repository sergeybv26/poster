from django.contrib import admin

from places.models import Place, PlaceImage


class ImageInlineAdmin(admin.TabularInline):
    model = PlaceImage
    exclude = ('uid', )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('uid',)
    inlines = [ImageInlineAdmin, ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    exclude = ('uid',)
