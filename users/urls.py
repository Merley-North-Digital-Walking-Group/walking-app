from django.urls import path
from . import views

urlpatterns = [
    path('login_email', views.login_email, name='login_email'),
    path('login_facebook', views.login_facebook, name='login_facebook'),
    path('login_google', views.login_google, name='login_google'),
    path('create_user', views.create_user, name='create_user'),
    path('user_homepage/<int:pk>/', views.user_homepage, name='user_homepage'),
    path('stepcounter', views.stepcounter, name='stepcounter'),
]