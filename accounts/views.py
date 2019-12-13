from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.decorators import login_required
from .models import User
from movies.models import Movie
from stars.models import Star, ProfileImg, Cast, Coworker
from .forms import CustomUserCreationForm
import random
from django.http import JsonResponse
from .serializers import UserSerializer
from stars.serializers import StarSerializer, CoworkerSerializer
from movies.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    users = get_user_model().objects.all()
    context = {
        'users': users
    }
    return render(request, 'accounts/index.html', context)


def detail(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movies = user.likemovies.all()
    stars = user.likestars.all()
    comment = user.comment_set.first()
    if comment:
        comment_casts = comment.movie.cast_set.all()
    else:
        comment_casts = []
    context = {
        'user': user,
        'movies': movies,
        'stars': stars,
        'comment': comment,
        'comment_stars': comment_casts,
    }
    return render(request, 'accounts/detail.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next') or 'accounts:index')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'],)
            auth_login(request, new_user)
            return redirect('accounts:pick')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/auth_page.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect(request.GET.get('next') or 'info:rec')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'info:rec')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/auth_page.html', context)


@login_required
def logout(request):
    auth_logout(request)
    return redirect('info:intro')


def follow(request, user_pk):
    if not request.user.is_authenticated:
        return redirect('accoutns:login')
    user = request.user
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if user == person:
        return redirect('accounts:detail', user_pk)
    if person.followers.filter(pk=user.pk).exists():
        person.followers.remove(user)
    else:
        person.followers.add(user)
    return redirect('accounts:detail', user_pk)

@login_required
def pick(request):
    user = request.user
    if user.likestars or user.likemovies:
        redirect('accounts:detail', user.pk)
    if request.method == "POST":
        pass
    else:
        movies = list(Movie.objects.all()[:30])
        randset = random.sample(movies, 12)
        castCandidate = []
        for i in randset:
            castCandidate += i.get_cast_order()
            print(i.get_cast_order())
        randcastset = random.sample(castCandidate, int(len(castCandidate) * 0.7))
        casts = [Cast.objects.get(pk=i).star for i in randcastset]
        pickset = casts + randset
        pickset = random.sample(pickset, len(pickset))
        context = {
            'pickset': pickset,
        }
        return render(request, 'accounts/pick.html', context)


def test(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=user_pk)
    movies = user.likemovies.all()
    stars = user.likestars.all()

    context = {
        'test':1,
    }
    return JsonResponse(context)



# Serailizer
@api_view(["GET"])
def user_detail(request, user_pk):
    user = get_object_or_404(User, pk=user_pk)
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def star_detail(request, star_pk):
    star = get_object_or_404(Star, pk=star_pk)
    serializer = StarSerializer(star)
    return Response(serializer.data)
    

@api_view(["GET"])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
    

@api_view(["GET"])
def movie_coworker(request, movie_pk):
    coworkers = Coworker.objects.all()
    coworker_set = []

    for coworker in coworkers:
        if coworker.movie_id == movie_pk:
            coworker_set.append(coworker)
    serializer = CoworkerSerializer(coworker_set, many=True)
    return Response(serializer.data)