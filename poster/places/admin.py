from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from places.models import Place, PlaceImage


class ImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    readonly_fields = ('image_preview',)
    extra = 1
    min_num = 0
    ordering = ['order']

    def image_preview(self, obj):
        return format_html('<img src="{}" width="{}" height={} style="height: 200px; width: auto" />',
                           obj.image.url, obj.image.width, obj.image.height
                           )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('uid',)
    inlines = (ImageInlineAdmin,)
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    exclude = ('uid',)
