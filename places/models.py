from django.db import models

# Create your models here.

class Places(models.Model):
    title = models.CharField(max_length=255)
    description_short = models.TextField()
    description_long = models.TextField()
    longitude = models.CharField(max_length=32)
    latitude = models.CharField(max_length=32)

    def __str__(self):
        return self.title
