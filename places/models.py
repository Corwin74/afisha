import uuid
from django.db import models
from django.utils.html import mark_safe
from tinymce.models import HTMLField

class Places(models.Model):
    title = models.CharField(max_length=255)
    place_id = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
    description_short = HTMLField()
    description_long = HTMLField()
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)

    class Meta:
        verbose_name='Место'
        verbose_name_plural='Места'

    def __str__(self):
        return self.title

class Images(models.Model):
    place = models.ForeignKey(Places, on_delete=models.CASCADE)
    id_pic = models.PositiveSmallIntegerField(
        default=1,
        blank=False,
        null=False
    )
    image = models.ImageField(upload_to='places_images/') 

    def __str__(self):
        return str(self.id_pic) + ' ' + str(self.place)

    @property
    def preview(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="200" />')
        return ""

    class Meta:
        ordering = ('id_pic',)
        verbose_name='Картинка'
        verbose_name_plural='Картинки'
