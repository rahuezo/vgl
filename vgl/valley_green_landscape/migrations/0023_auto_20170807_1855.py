# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-08 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley_green_landscape', '0022_auto_20170725_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.ImageField(default='D:\\Google Drive\\Programming Projects\\web_dev\\vgl\\vgl\\media\\no-img.png', upload_to=b'D:\\Google Drive\\Programming Projects\\web_dev\\vgl\\vgl\\media'),
        ),
    ]