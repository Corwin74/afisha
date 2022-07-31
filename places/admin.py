from django.contrib import admin
from django.utils.html import mark_safe
from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from .models import Place, Image


class ImageInline(SortableTabularInline):
    model = Image
    fields = ('place', 'image', 'preview_image', 'order_num')
    readonly_fields = ('preview_image',)
    extra = 0

    def preview_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" height="200" />')


class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title', ]


admin.site.register(Place, PlacesAdmin)
