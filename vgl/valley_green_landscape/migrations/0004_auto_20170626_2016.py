# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-27 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley_green_landscape', '0003_auto_20170626_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.CharField(default='http://s3.amazonaws.com/hpi-production/avatars/19/default/anonymous-user-gravatar.png?1398350512', max_length=1024),
        ),
    ]