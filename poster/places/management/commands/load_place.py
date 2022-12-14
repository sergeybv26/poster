import os.path
from urllib.parse import urlparse

import requests
from django.conf import settings
from django.core.files import File
from django.core.management import BaseCommand

from places.models import Place, PlaceImage


def get_place_data(link, img_flag=False):
    """
    Загружает данные по ссылке
    :param link: Ссылка
    :param img_flag: Флаг о загрузке изображения
    :return: Байты
    """
    response = requests.get(link)
    if response.status_code == 200:
        if not img_flag:
            return response.json()
        return response.content


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Загрузка данных о местах из JSON файлов.

        link = options['link']

        place_json = get_place_data(link)
        if not os.path.isdir(f'{settings.BASE_DIR}/media/places/'):
            os.makedirs(f'{settings.BASE_DIR}/media/places/')
        if isinstance(place_json, dict):
            print(f"Загрузка информации о месте: {place_json['title']}")
            place, _ = Place.objects.get_or_create(
                title=place_json['title'],
                description_short=place_json['description_short'],
                description_long=place_json['description_long'],
                latitude=float(place_json['coordinates']['lat']),
                longitude=float(place_json['coordinates']['lng'])
            )
            # Выполняем загрузку изображений
            for img_link in place_json['imgs']:
                image_data = get_place_data(img_link, img_flag=True)
                filename = os.path.basename(urlparse(img_link).path)
                with open(f'{settings.BASE_DIR}/media/places/{filename}', 'wb') as f:
                    f.write(image_data)
                image_file = open(f'{settings.BASE_DIR}/media/places/{filename}', 'rb')
                django_file = File(image_file)
                place_image = PlaceImage()
                place_image.place = place
                place_image.image.save(filename, django_file, save=True)

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='Link to JSON with location data')
