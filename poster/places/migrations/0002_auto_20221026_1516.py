# Generated by Django 3.2.16 on 2022-10-26 12:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='places', verbose_name='Изображение')),
                ('order', models.IntegerField(verbose_name='Ранг изображения')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='placeimg', to='places.place', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
    ]