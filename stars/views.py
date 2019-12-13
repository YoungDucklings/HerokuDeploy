from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Star, ProfileImg, Cast
from movies.models import Poster
from accounts.models import User
from collections import OrderedDict
from .forms import StarForm, ProfileImgForm, TagedImgForm


@login_required
def index(request):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    stars = Star.objects.all()
    context = {
        'stars': stars,
    }
    return render(request, 'stars/index.html', context)


def detail(request, star_id):
    star = Star.objects.get(pk=star_id)
    casts = Cast.objects.filter(star=star_id)
    posters = []
    for cast in casts:
        posters.append(Poster.objects.filter(movie=cast.movie).first())
    context = {
        'star': star,
        'posters': posters,
    }
    return render(request, 'stars/detail.html', context)


@login_required
def create(request):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    if request.method == 'POST':
        form = StarForm(request.POST)

        if form.is_valid():
            star = form.save()
            star.save()

            return redirect('stars:index')

    form = StarForm()

    context = {
        'form': form,
    }
    return render(request, 'stars/create.html', context)


## 수정 필요
@login_required
def update(request, star_id):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    star = Star.objects.get(pk=star_id)

    if request.method == 'POST':
        form = StarForm(request.POST, instance=star)
        if form.is_valid():
            star.save()
            return redirect('stars:detail', star_id)

    form = StarForm(instance=star)
    context = {
        'star': star,
        'form': form,
    }
    return render(request, 'stars/update.html', context)

@login_required
@require_POST
def delete(request, star_id):
    if request.user != User.objects.get(pk=1):
        return redirect('accounts:login')

    if request.method == 'POST':
        star = Star.objects.get(pk=star_id)
        star.delete()
        return redirect('stars:index')


@login_required
def like(request, star_id):
    star = Star.objects.get(pk=star_id)
    user = request.user

    if star.user_set.filter(pk=user.pk).exists():
        star.user_set.remove(user)
        liked = False
    else:
        star.user_set.add(user)
        liked = True
    context = {
        'liked': liked,
        'count': star.user_set.count(),
    }
    return JsonResponse(context)
