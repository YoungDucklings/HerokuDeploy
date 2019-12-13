from django.shortcuts import render
from stars.models import Star
from movies.models import Movie
from accounts.models import User
from django.contrib.auth.decorators import login_required
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
