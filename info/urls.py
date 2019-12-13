from django.urls import path
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.intro, name='intro'),
    path('search/', views.search, name='search'),
    path('rec/', views.rec, name='rec'),
]