# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley_green_landscape', '0011_gallerycontainer_galleryimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='galleryimage',
            name='image_path',
            field=models.CharField(default=0, max_length=1000),
            preserve_default=False,
        ),
    ]