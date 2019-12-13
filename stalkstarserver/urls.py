"""stalkstarserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from accounts import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('info.urls')),
    path('admin/', admin.site.urls),
    path('stars/', include('stars.urls')),
    path('movies/', include('movies.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/v1/accounts/<int:user_pk>/', views.user_detail),
    path('api/v1/stars/<int:star_pk>/', views.star_detail),
    path('api/v1/movies/<int:movie_pk>/', views.movie_detail),
    path('api/v1/coworkers/<int:movie_pk>/', views.movie_coworker),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)