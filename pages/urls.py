from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('weather', views.weather, name='weather'),
    path('news', views.news, name='news'),
    path('', include('users.urls')),
]