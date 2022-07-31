from django.core.management.base import BaseCommand
import requests
from places.models import Place, Image
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Add place to map from json file'

    def add_arguments(self, parser):
        parser.add_argument('url', help='URL to download json file with place description')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        try:    
            place_import_data = response.json()
        except requests.exceptions.JSONDecodeError:
            print('Error import file -- Bad JSON format!')
            return
        try:
            title = place_import_data['title']               
            lng, lat = place_import_data['coordinates']['lng'], place_import_data['coordinates']['lat']
        except KeyError as exc:
            print(f'Error import file -- Missing key: {exc}')
            return
        imgs = place_import_data.get('imgs', [])
        desc_short = place_import_data.get('description_short', '')
        desc_long = place_import_data.get('description_long', '')
        place, is_created = Place.objects.get_or_create(
            title=title,
            defaults={
                      'description_short': desc_short,
                      'description_long': desc_long,
                      'latitude': lat,
                      'longitude': lng
            }
        )
        if is_created:
            for index, img in enumerate(imgs, 1):
                response = requests.get(img)
                response.raise_for_status()

                image_content = ContentFile(response.content, name=f'{index} {place.pk}.jpg')
                place_image_obj = Image.objects.create(
                    place=place,
                    order_num=index,
                    image=image_content
                )
        else:
            print(f'Place "{title}" exist in database!')
