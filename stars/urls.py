from django.urls import path
from . import views

app_name = 'stars'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:star_id>/', views.detail, name='detail'),
    path('create/', views.create, name="create"),
    path('<int:star_id>/update/', views.update, name="update"),
    path('<int:star_id>/delete/', views.delete, name="delete"),
    path('<int:star_id>/like/', views.like, name='like')
]