from django.urls import path
from . import views

urlpatterns = [
    path('walks_list', views.walks_list, name='walks_list'),
    path('walks_detail/<int:pk>/', views.walks_detail, name='walks_detail'),
]