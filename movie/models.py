from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    likes = models.IntegerField(default=0)
