from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_pk>/', views.detail, name='detail'),
    path('pick/', views.pick, name='pick'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
    # path('test/<int:user_pk>/', views.test, name='test'),
]