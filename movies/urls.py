from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/update/', views.update, name='update'),
    path('<int:movie_id>/delete/', views.delete, name='delete'),
    path('<int:movie_id>/comment_create/', views.comment_create, name='comment_create'),
    path('<int:movie_id>/comment_delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('<int:movie_id>/<int:n>/rate/', views.rate, name="rate"),
    path('<int:movie_id>/score/', views.score, name="score"),
]