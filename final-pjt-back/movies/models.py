from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Top_Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    year = models.IntegerField()
    ranking = models.IntegerField()


class Now_Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)
    backdrop_path = models.CharField(max_length=200)
    genres = models.ManyToManyField(Genre)
    year = models.IntegerField()
    ranking = models.IntegerField()