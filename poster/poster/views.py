from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def get_main_page(request):
    """Представление для отображения главной страницы"""
    places = Place.objects.all()

    places_info = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.uid,
                    'detailsUrl': reverse('place_api', args=[place.uid])
                }
            } for place in places
        ]
    }
    context = {
        'geojson': places_info
    }

    return render(request, 'index.html', context=context)


def get_places(request, pk):
    """
    Представление JSON API.
    :param request: запрос
    :param pk: id достопримечательности
    :return: HTTP Response - достопримечательность
    """
    place = get_object_or_404(Place, pk=pk)
    place_info = {
        'title': place.title,
        'imgs': [img.image.url for img in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lng': place.longitude,
            'lat': place.latitude
        }
    }

    return JsonResponse(place_info, json_dumps_params={'indent': 2, 'ensure_ascii': False})
