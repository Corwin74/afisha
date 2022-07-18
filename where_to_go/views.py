from django.shortcuts import render

places = [{'title': 'Легенды Москвы', 'place_id': 'moscow_legends',
           'details_url': '/static/places/moscow_legends.json',
           'longitude': 37.62, 'latitude': 55.793676},
           {'title': 'Крыши24.рф', 'place_id': 'roofs24',
           'details_url': '/static/places/roofs24.json',
           'longitude': 37.64, 'latitude': 55.753676}]

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

geo_features = [make_geo_feature(place['title'], place['place_id'], place['longitude'],
                place['latitude'], place['details_url']) for place in places]

geo_json = {'type': 'FeatureCollection', 'features': geo_features}

def start_page(request):
    return render(request, 'index.html', context={'value': geo_json})
