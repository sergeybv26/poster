from uuid import uuid4

from ckeditor.fields import RichTextField
from django.db import models


class Place(models.Model):
    """Модель сущности Достопримечательность"""
    uid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=512, unique=True, verbose_name='Наименование')
    description_short = models.CharField(max_length=512, blank=True, null=True, verbose_name='Краткое описание')
    description_long = RichTextField(verbose_name='Полное описание')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class PlaceImage(models.Model):
    """Модель сущности Изображение достопримечательности"""
    uid = models.UUIDField(primary_key=True, default=uuid4)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='placeimg', verbose_name='Место')
    image = models.ImageField(upload_to='places', verbose_name='Изображение')
    order = models.IntegerField(verbose_name='Ранг изображения')

    def __str__(self):
        return f'{self.order} {self.place}'

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
