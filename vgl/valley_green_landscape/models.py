from __future__ import unicode_literals

from django.db import models
import datetime


class Review(models.Model):
    user = models.CharField(max_length=100)
    photo = models.CharField(max_length=1024,
                             default="https://raw.githubusercontent.com/rahuezo/vgl/master/vgl/valley_green_landscape/static/valley_green_landscape/img/anonymous_user.gif")
    text = models.CharField(max_length=1024)
    score = models.IntegerField(default=5)
    star_score = models.CharField(max_length=1000)
    posted_at = models.DateField(default=datetime.date.today)






