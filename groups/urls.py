from django.urls import path
from . import views

urlpatterns = [
    path('group_details/<int:pk>/', views.group_details, name= 'group_details'),
]