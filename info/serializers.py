from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.models import Movie
from stars.models import Star, Coworker, ProfileImg, Cast


class MovieInfoSerializer(serializers.ModelSerializer):
    poster_set = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Movie
        fields = ('pk', 'title', 'poster_set',)


class StarInfoSerializer(serializers.ModelSerializer):
    profileimg_set = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Star
        fields = ('pk', 'name', 'profileimg_set',)


class CoworkerSerializer(serializers.ModelSerializer):
    movie = MovieInfoSerializer()
    from_star = serializers.StringRelatedField()
    to_star = StarInfoSerializer()
    
    class Meta:
        model = Coworker
        fields = ('movie', 'from_star', 'to_star',)


class StarSerializer(serializers.ModelSerializer):
    profileimg_set = serializers.StringRelatedField(many=True)
    coworker_from = CoworkerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Star
        fields = ('pk', 'name', 'profileimg_set', 'coworker_from',)


class UserSerializer(serializers.ModelSerializer):
    likestars = StarSerializer(many=True, read_only=True)
    likemovies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'likestars', 'likemovies',)
      
