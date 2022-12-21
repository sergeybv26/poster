import os.path
from urllib.parse import urlparse

import requests

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

        place, place_created = self.create_place(place_info)

        if not place:
            return None
        if not place_created:
            print(f"Обновлена информация о месте: {place_info.get('title')}. Загрузка фотографий не выполнялась")
            return None

        self.create_images(place_info, place, place_created)

    def add_arguments(self, parser):
        parser.add_argument('link', type=str, help='Link to JSON with location data')

    def create_place(self, place_info: dict):
        """Создает запись в БД о месте"""
        title = place_info.get('title')
        if not title:
            print('В файле JSON отсутствует обязательное поле title')
            return None, None

        try:
            latitude = float(place_info['coordinates']['lat'])
            longitude = float(place_info['coordinates']['lng'])
        except KeyError:
            print('В файле JSON отсутствуют координаты места')
            return None, None
        print(f"Загрузка информации о месте: {title}")
        place, place_created = Place.objects.get_or_create(
            title=title,
            defaults={
                'description_short': place_info.get('description_short', ''),
                'description_long': place_info.get('description_long', ''),
                'latitude': latitude,
                'longitude': longitude
            }
        )
        return place, place_created

    def create_images(self, place_info: dict, place: Place, place_created: bool):
        """
        Создает запись в БД о изображениях места
        :param place_info: словарь с информацией о месте
        :param place: объект модели Place
        :param place_created: флаг создания новой записи о месте
        :return: None
        """

        for order, img_link in enumerate(place_info.get('imgs', [])):
            image = requests.get(img_link)
            if not image.ok:
                return None
            image = image.content
            filename = os.path.basename(urlparse(img_link).path)
            django_file = ContentFile(image, name=filename)
            PlaceImage.objects.create(place=place, image=django_file, order=order)
