from rest_framework import serializers
from .models import Movie
from django.contrib.auth import get_user_model
from stars.serializers import CoworkerSerializer

class MovieSerializer(serializers.ModelSerializer):
    coworker_set = CoworkerSerializer(many=True)
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'coworker_set',)
