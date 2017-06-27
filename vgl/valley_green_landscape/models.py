from __future__ import unicode_literals

from django.db import models
import datetime


class Review(models.Model):
    user = models.CharField(max_length=100)
    photo = models.CharField(max_length=1024,
                             default="{% static 'valley_green_landscape:anonymous_user.gif'%}")
    text = models.CharField(max_length=1024)
    posted_at = models.DateField(default=datetime.date.today)





