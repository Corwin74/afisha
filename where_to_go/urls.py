from django.contrib import admin
from django.urls import path
from .views import start_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_page),
]
