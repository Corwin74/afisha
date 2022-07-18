from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import start_page, place_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('places/<int:place_id>', place_detail, name='place_detail'),
    path('', start_page),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
