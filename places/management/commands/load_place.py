from django.core.management.base import BaseCommand
import requests
from places.models import Places, Images
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Add place to map from json file'

    def add_arguments(self, parser):
        parser.add_argument('url', help='URL to download json file with place decription')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()

        place = response.json()
        title = place['title']
        imgs = place['imgs']
        desc_short = place['description_short']
        desc_long = place['description_long']
        lng, lat = place['coordinates'].values()

        place, _ = Places.objects.get_or_create(
            title=title,
            description_short=desc_short,
            description_long=desc_long,
            latitude=lat,
            longitude=lng
        )

        for idx, img in enumerate(imgs, 1):
            response = requests.get(img)
            response.raise_for_status()

            image_content = ContentFile(response.content)
            place_image_obj = Images.objects.create(
                place=place,
                id_pic=idx
            )

            place_image_obj.image.save(f'{idx} {place.pk}.jpg', image_content, save=True)