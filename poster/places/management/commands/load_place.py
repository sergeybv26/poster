import os.path
from urllib.parse import urlparse

import requests
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.management import BaseCommand

from places.models import Place, PlaceImage


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Загрузка данных о местах из JSON файлов.

        link = options['link']

        place_info = requests.get(link)
        if not place_info.ok:
            return None
        place_info = place_info.json()

        if not isinstance(place_info, dict):
            return None

        title = place_info.get('title', '')
        coordinates = place_info.get('coordinates', {})

        print(f"Загрузка информации о месте: {title}")
        place, place_created = Place.objects.get_or_create(
            title=title,
            defaults={
                'description_short': place_info.get('description_short', ''),
                'description_long': place_info.get('description_long', ''),
                'latitude': float(coordinates.get('lat', 0)),
                'longitude': float(coordinates.get('lng', 0))
            }
        )
        if not place_created:
            PlaceImage.objects.filter(place=place).delete()

        # Выполняем загрузку изображений
        for img_link in place_info.get('imgs', []):
            image = requests.get(img_link)
            if not image.ok:
                return None
            image = image.content
            filename = os.path.basename(urlparse(img_link).path)
            django_file = ContentFile(image, name=f'{settings.BASE_DIR}/media/places/{filename}')
            place_image = PlaceImage()
            place_image.place = place
            place_image.image.save(filename, django_file, save=True)

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='Link to JSON with location data')
