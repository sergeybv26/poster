from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from places.models import Place


def main(request):
    """Представление для отображения главной страницы"""
    places = Place.objects.all()

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
                    'detailsUrl': 'static/places/moscow_legends.json'
                    if item.title == 'Экскурсионная компания «Легенды Москвы»' else 'static/places/roofs24.json'
                }
            } for item in places
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

    return HttpResponse(place.title)
