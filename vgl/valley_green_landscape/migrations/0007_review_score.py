# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-27 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley_green_landscape', '0006_auto_20170626_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='score',
            field=models.IntegerField(default=5),
        ),
    ]