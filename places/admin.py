from django.contrib import admin
from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from .models import Places, Images

class ImageInline(SortableTabularInline):
    model = Images
    fields = ('place', 'image', 'preview_image', 'id_pic')
    readonly_fields = ('preview_image',)
    extra = 0


    def preview_image(self, obj):
        return obj.preview


class PlacesAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title',]

admin.site.register(Places, PlacesAdmin)
