from adminsortable2.admin import SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, PlaceImage


class ImageInlineAdmin(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    exclude = ('uid',)
    readonly_fields = ('image_preview',)
    extra = 1
    ordering = ['order']

    def image_preview(self, obj):
        return format_html(
            '{}', mark_safe(
                f'<img src="{obj.image.url}" '
                f'width="{obj.image.width}" height={obj.image.height}'
                f' style="height: 200px; width: auto" />'
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('uid',)
    inlines = [ImageInlineAdmin, ]
    search_fields = ['title']


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    exclude = ('uid',)
