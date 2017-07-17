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
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.user

    def __unicode__(self):
        return self.user

class GalleryContainer(models.Model):
    container_title = models.CharField(max_length=100)
    badge_code = models.CharField(max_length=10000)

class GalleryImage(models.Model):
    container = models.ForeignKey(GalleryContainer, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=1000)
    description = models.CharField(max_length=250)
