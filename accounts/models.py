from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse
from movies.models import Movie
from stars.models import Star

# Create your models here.
class User(AbstractUser):
    likemovies = models.ManyToManyField(Movie, blank=True)
    likestars = models.ManyToManyField(Star, blank=True)
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings', blank=True)

    class Meta:
        ordering = ['-pk']

    def get_absolute_url(self):
        return reverse('accounts:detail', kwargs={'user_pk': self.pk})
    
    def __str__(self):
        return self.username


class Comment(models.Model):
    stalker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    likestalkers = models.ManyToManyField(User, related_name='likecomments', blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.content


class Score(models.Model):
    stalker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    score = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return str(self.score)