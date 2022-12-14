# Generated by Django 3.2.16 on 2022-12-14 08:39

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, default=django.utils.timezone.now, verbose_name='Полное описание'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='place',
            name='description_short',
            field=models.TextField(blank=True, default=django.utils.timezone.now, verbose_name='Краткое описание'),
            preserve_default=False,
        ),
    ]
