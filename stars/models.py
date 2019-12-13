from django.db import models
from movies.models import Movie
from django.urls import reverse

# Create your models here.

class Star(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    deathday = models.DateField()
    department = models.CharField(max_length=50)
    biography = models.TextField()
    homepage = models.TextField()

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('stars:detail', kwargs={'star_pk': self.pk})
    
    def __str__(self):
        return self.name


class ProfileImg(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    url = models.TextField()

    def __str__(self):
        return self.url


class TagedImg(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    backdrops = models.TextField()
    posters = models.TextField()


class Coworker(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    from_star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name="coworker_from")
    to_star = models.ForeignKey(Star, on_delete=models.CASCADE, related_name="coworker_to")


class Cast(models.Model):
    star = models.ForeignKey(Star, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    character = models.CharField(max_length=100)
    
    class Meta:
        order_with_respect_to = 'movie'