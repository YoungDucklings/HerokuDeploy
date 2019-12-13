from rest_framework import serializers
from .models import Star, Coworker
from django.contrib.auth import get_user_model

class CoworkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coworker
        fields = ('pk', 'movie', 'from_star', 'to_star',)


class StarSerializer(serializers.ModelSerializer):
    coworker_from = CoworkerSerializer(many=True)
    coworker_to = CoworkerSerializer(many=True)
    class Meta:
        model = Star
        fields = ('pk', 'name', 'coworker_from', 'coworker_to',)
