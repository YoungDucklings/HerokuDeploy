from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from rest_framework.response import Response
from rest_framework.decorators import api_view

from accounts.models import User
from movies.models import Movie
from stars.models import Star, ProfileImg, Cast, Coworker

from django.http import JsonResponse
from .serializers import UserSerializer

# Create your views here.

def intro(request):
    return render(request, 'info/intro.html')

    
def search(request):
    q = request.GET.get('query', '')
    stars, movies, users = [], [], []
    if q == 'stars':
        stars = Star.objects.all()
    elif q == 'movies':
        movies = Movie.objects.all()

    elif q == 'users':
        users = User.objects.all()
    else:
        stars = Star.objects.filter(name__icontains=q)
        movies = Movie.objects.filter(title__icontains=q) or Movie.objects.filter(original_title__icontains=q)
        users = User.objects.filter(username__icontains=q)

    context = {
        'stars': stars,
        'movies': movies,
        'users': users,
    }
    return render(request, 'info/search.html', context)


@login_required
def rec(request):
    user = request.user
    stars = user.likestars.all()
    movies = user.likemovies.all()
    popular = Movie.objects.all()[:30]
    context = {
        'user': user,
        'stars': stars,
        'movies': movies,
        'popular':popular,
    }
    return render(request, 'info/rec.html', context)


# Serailizer
@api_view(["GET"])
def user_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


# @api_view(["GET"])
# def star_detail(request, star_pk):
#     star = get_object_or_404(Star, pk=star_pk)
#     serializer = StarSerializer(star)
#     return Response(serializer.data)
    

# @api_view(["GET"])
# def movie_detail(request, movie_pk):
#     movie = get_object_or_404(Movie, pk=movie_pk)
#     serializer = MovieSerializer(movie)
#     return Response(serializer.data)
    

# @api_view(["GET"])
# def movie_coworker(request, movie_pk):
    coworkers = Coworker.objects.all()
    coworker_set = []

    for coworker in coworkers:
        if coworker.movie_id == movie_pk:
            coworker_set.append(coworker)
    serializer = CoworkerSerializer(coworker_set, many=True)
    return Response(serializer.data)