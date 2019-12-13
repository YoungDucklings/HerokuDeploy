from django.db import models
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=50)
    original_title = models.CharField(max_length=50)
    genres = models.ManyToManyField(Genre)
    release_date = models.DateField()
    # ModelForm -> input_frmats=settings.DATE_INPUT_FORMATS
    runtime = models.IntegerField()
    status = models.CharField(max_length=20)
    vote_average = models.FloatField()
    adult = models.BooleanField()
    belongs_to_collection = models.IntegerField()
    original_language = models.CharField(max_length=20)
    homepage = models.TextField()
    overview = models.TextField()

    class Meta:
        ordering = ['-vote_average']

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'movie_pk': self.pk})
    
    def __str__(self):
        return self.title


class Backdrop(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    url = models.TextField()

    def __str__(self):
        return self.url

class Poster(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    url = models.TextField()

    def __str__(self):
        return self.url


class Video(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    url = models.TextField()

    def __str__(self):
        return self.url