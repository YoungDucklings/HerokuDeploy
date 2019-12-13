from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from stars.models import Cast
from .models import Movie, Poster, Video, Backdrop
from accounts.models import User, Comment, Score
from .forms import CommentForm, MovieForm, PosterForm, BackdropForm, VideoForm

# Create your views here.

@login_required
def index(request):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    movies = Movie.objects.all()
    context = {
        'movies': movies,
    }
    return render(request, 'movies/index.html', context)


def detail(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    backdrops = Backdrop.objects.filter(movie=movie_id)
    posters = Poster.objects.filter(movie=movie_id)
    videos = Video.objects.filter(movie=movie_id)
    comments = Comment.objects.filter(movie=movie_id)
    if Score.objects.filter(movie=movie, stalker=request.user).exists():
        score = Score.objects.get(movie=movie, stalker=request.user).score
    else:
        score = 0

    comment_form = CommentForm()

    context = {
        'movie': movie,
        'backdrops': backdrops,
        'posters': posters,
        'videos': videos,
        'score': score,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'movies/detail.html', context)

@login_required
def comment_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.stalker = request.user
            comment.movie = movie
            comment.save()
    
    return redirect('movies:detail', movie_id)

@login_required
@require_POST
def comment_delete(request, movie_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    comment.delete()
    return redirect('movies:detail', movie_id)



@login_required
def create(request):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    if request.method == 'POST':
        form = MovieForm(request.POST)

        if form.is_valid():
            movie = form.save()
            movie.save()

        return redirect('movies:index')

    form = MovieForm()

    context = {
        'form': form,
    }
    return render(request, 'movies/create.html', context)


## 수정 필요
@login_required
def update(request, movie_id):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    movie = Movie.objects.get(pk=movie_id)

    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie.save()
            return redirect('movies:detail', movie_id)

    form = MovieForm(instance=movie)
    context = {
        'movie': movie,
        'form': form,
    }
    return render(request, 'movies/update.html', context)

@login_required
@require_POST
def delete(request, movie_id):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    if request.method == 'POST':
        movie = Movie.objects.get(pk=movie_id)
        movie.delete()
        return redirect('movies:index')

# 별점 주기
# 별점이 있을 때
# if Score.objects.filter(movie=movie).filter(stalker=user).exists()
# score = Score.objects.filter(movie=movie).filter(stalker=user).score
# score.score = n
# score.save()
# 별점이 없을 때
# Score.objects.create(stalker=user, score=n, movie=movie)


# 디폴트 세팅(별점이 없을 때만)
# if Score.objects.filter(movie=movie).filter(stalker=user).exists()
# score = 0

@login_required
def rate(request, movie_id, n):
    movie = Movie.objects.get(pk=movie_id)
    user = request.user
    user.likemovies.add(movie_id)
    if Score.objects.filter(movie=movie).filter(stalker=user).exists():
        new_score = Score.objects.get(movie=movie, stalker=user)
        new_score.score = n
        new_score.save()
    else:
        Score.objects.create(stalker=user, score=n, movie=movie)
    context = {
        'score':n
    }
    return JsonResponse(context)

def score(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    user = request.user
    if Score.objects.filter(movie=movie).filter(stalker=user).exists():
        rate = Score.objects.get(movie=movie, stalker=user).score
    else:
        rate = 0
    context = {
        'rate': rate
    }
    return JsonResponse(context)