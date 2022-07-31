from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from places.models import Place


def make_geo_feature(title, place_id, longitude, latitude, details_url):
    properties_feature = {'title': title,
                          'placeId': place_id,
                          'detailsUrl': details_url
                          }

    geometry_feature = {'type': 'Point',
                        'coordinates': [longitude, latitude]
                        }

    return {'type': 'Feature',
            'geometry': geometry_feature,
            'properties': properties_feature
            }


def start_page(request):
    places = Place.objects.all()
    geo_features = [
        make_geo_feature(
                        place.title,
                        place.id,
                        float(place.longitude),
                        float(place.latitude),
                        reverse('place_detail', args=(place.pk,)),
        )
        for place in places
                    ]
    geo_json = {'type': 'FeatureCollection', 'features': geo_features}

    return render(request, 'index.html', context={'value': geo_json})


def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    place_detail_response = {
        'title': place.title,
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
                        'lat': place.latitude,
                        'lng': place.longitude,
        },
        'imgs': [img.image.url for img in place.images.all()],
    }

    return JsonResponse(place_detail_response,
                        json_dumps_params={'ensure_ascii': False,
                                           'indent': 2})
