from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
from .models import User
from movies.models import Movie
from stars.models import Star, ProfileImg, Cast, Coworker
from .forms import CustomUserCreationForm
import random



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
    scores = user.score_set.all()
    popular = Movie.objects.all()[:30]
    scoreli = [0,0,0,0,0]
    scoresum = 0
    for s in scores:
        scoreli[s.score-1] += 1
        scoresum += s.score
    if scoresum:
        average = round(scoresum/(len(scores)), 2)
        scoreli = [int(s/len(scores)*100) if int(s/len(scores)*100)>10 else 10 for s in scoreli]
    else:
        average = 0
        scoreli = [10,10,10,10,10]
    stars = user.likestars.all()
    comment = user.comment_set.first()
    if comment:
        comment_casts = comment.movie.cast_set.all()
    else:
        comment_casts = []
    context = {
        'user': user,
        'movies': movies,
        'popular': popular,
        'stars': stars,
        'comment': comment,
        'comment_stars': comment_casts,
        'scoreli':scoreli,
        'average':average,
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
        return redirect(request.GET.get('next') or 'info:intro')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'info:intro')
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
        randcastset = random.sample(castCandidate, int(len(castCandidate) * 0.7))
        casts = [Cast.objects.get(pk=i).star for i in randcastset]
        pickset = casts + randset
        pickset = random.sample(pickset, len(pickset))
        context = {
            'pickset': pickset,
        }
        return render(request, 'accounts/pick.html', context)


# def test(request, user_pk):
#     user = get_object_or_404(get_user_model(), pk=user_pk)
#     movies = user.likemovies.all()
#     stars = user.likestars.all()

#     context = {
#         'test':1,
#     }
#     return JsonResponse(context)