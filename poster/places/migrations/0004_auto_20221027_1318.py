# Generated by Django 3.2.16 on 2022-10-27 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='placeimage',
            options={'ordering': ['order'], 'verbose_name': 'Изображение', 'verbose_name_plural': 'Изображения'},
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Ранг изображения'),
        ),
    ]
