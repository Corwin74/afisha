from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from places.models import Places, Images


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
    places = Places.objects.all()
    geo_features = [make_geo_feature(place.title, place.place_id, float(place.longitude),
                float(place.latitude), '/places/' + str(place.pk)) for place in places]
    geo_json = {'type': 'FeatureCollection', 'features': geo_features}
    return render(request, 'index.html', context={'value': geo_json})

def place_detail(request, place_id):
    place_detail_response = {}
    place = get_object_or_404(Places, pk=place_id)
    place_detail_response['title'] = place.title
    place_detail_response['imgs'] = []
    place_detail_response['description_short'] = place.description_short
    place_detail_response['description_long'] = place.description_long
    place_detail_response['coordinates'] = {'lat': place.latitude, 'lng': place.longitude}
    images = Images.objects.filter(place=place)
    place_detail_response['imgs'] = [img.image.url for img in images]
    return JsonResponse(place_detail_response, json_dumps_params={'ensure_ascii': False,
                                                                   'indent': 2})
