# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-14 07:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley_green_landscape', '0012_galleryimage_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallerycontainer',
            name='badge_code',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
