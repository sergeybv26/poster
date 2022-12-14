from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from places.models import Place


def get_geojson(item):
    """
    Формирует и возвращает Geo JSON для объекта достопримечательности
    :param item: экземпляр класса Place
    :return: Geo JSON
    """
    geojson = {
        'title': item.title,
        'imgs': [img.image.url for img in item.images.all()],
        'description_short': item.description_short,
        'description_long': item.description_long,
        'coordinates': {
            'lng': item.longitude,
            'lat': item.latitude
        }
    }
    return geojson


def main(request):
    """Представление для отображения главной страницы"""
    queryset = Place.objects.all()

    geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [item.longitude, item.latitude]
                },
                'properties': {
                    'title': item.title,
                    'placeId': item.uid,
                    'detailsUrl': reverse('place_api', args=[item.uid])
                }
            } for item in queryset
        ]
    }
    context = {
        'geojson': geojson
    }

    return render(request, 'index.html', context=context)


def places(request, pk):
    """
    Представление JSON API.
    :param request: запрос
    :param pk: id достопримечательности
    :return: HTTP Response - достопримечательность
    """
    place = get_object_or_404(Place, pk=pk)
    geojson = get_geojson(place)

    return JsonResponse(geojson)
