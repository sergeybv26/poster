from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from places.models import Place, PlaceImage


class ImageInlineAdmin(admin.TabularInline):
    model = PlaceImage
    exclude = ('uid',)
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return format_html(
            '{}', mark_safe(
                f'<img src="{obj.get_absolute_image_url}" '
                f'width="{obj.image.width}" height={obj.image.height}'
                f' style="height: 200px; width: auto" />'
            )
        )


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    exclude = ('uid',)
    inlines = [ImageInlineAdmin, ]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    exclude = ('uid',)
