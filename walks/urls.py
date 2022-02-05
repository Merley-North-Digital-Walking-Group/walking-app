from django.urls import path
from . import views

urlpatterns = [
    path('walks', views.walks, name='walks'),
]