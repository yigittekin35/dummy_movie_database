from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    rank = models.FloatField(default=0.0)