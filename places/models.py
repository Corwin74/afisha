from django.db import models
from django.utils.html import mark_safe

class Places(models.Model):
    title = models.CharField(max_length=255)
    place_id = models.CharField(max_length=128, blank=True)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)

    def __str__(self):
        return self.title

class Images(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    id_pic = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='places_images/')

    def __str__(self):
        return str(self.id_pic) + ' ' + str(self.place)

    @property
    def preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="200" />')
        return ""
