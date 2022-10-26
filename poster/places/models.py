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

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
