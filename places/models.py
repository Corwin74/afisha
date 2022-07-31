from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description_short = HTMLField(blank=True)
    description_long = HTMLField(blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7)
    latitude = models.DecimalField(max_digits=10, decimal_places=7)

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(
                             Place,
                             on_delete=models.CASCADE,
                             related_name='images'
    )
    order_num = models.PositiveSmallIntegerField(default=1)
    image = models.ImageField(upload_to='places_images/')

    def __str__(self):
        return f'{self.order_num} {self.place}'

    class Meta:
        ordering = ('order_num',)
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'
