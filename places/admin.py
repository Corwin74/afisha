from django.utils.html import format_html
from django.contrib import admin
from .models import Places, Images

class ImageInline(admin.TabularInline):
    model = Images
    fields = ('place', 'image', 'preview_image', 'id_pic',)
    readonly_fields = ('preview_image',)


    def preview_image(self, obj):
        return obj.preview


class PlacesAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]

admin.site.register(Places, PlacesAdmin)
