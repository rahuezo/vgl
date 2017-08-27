from __future__ import unicode_literals

from django.db import models
import datetime
from django.conf import settings
import os


class User(models.Model):
    username = models.CharField(max_length=100)
    review_key = models.CharField(max_length=6)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # photo = models.ImageField(upload_to=settings.MEDIA_ROOT, default='no-img.png')
    text = models.CharField(max_length=1024)
    score = models.IntegerField(default=5)
    star_score = models.CharField(max_length=1000)
    posted_at = models.DateField(default=datetime.date.today)
    verified = models.BooleanField(default=False)
    review_key = models.CharField(max_length=6, default='NO KEY')

    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username




