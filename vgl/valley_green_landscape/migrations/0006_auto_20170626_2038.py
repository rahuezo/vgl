# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-06-27 03:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('valley_green_landscape', '0005_auto_20170626_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='photo',
            field=models.CharField(default='https://raw.githubusercontent.com/rahuezo/vgl/master/vgl/valley_green_landscape/static/valley_green_landscape/img/anonymous_user.gif', max_length=1024),
        ),
    ]