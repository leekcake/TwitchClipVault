import datetime

from django.db import models

# Create your models here.


class Clip(models.Model):
    Title = models.CharField(max_length=400)
    CreatedAt = models.DateTimeField('video created')
    LengthInSecond = models.FloatField()
    ViewCount = models.IntegerField()
    VideoId = models.CharField(max_length=100)

    def CreatedAtString(self):
        return (self.CreatedAt + datetime.timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return self.Title