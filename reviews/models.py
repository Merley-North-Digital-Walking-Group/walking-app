from datetime import date
from operator import mod
from statistics import mode
from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from users.models import App_User
from walks.models import Walk

class Review(models.Model):
    walk_title = models.ForeignKey(Walk, on_delete=models.CASCADE, default=0)
    author = models.ForeignKey(App_User, on_delete=models.CASCADE, default=0)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=3000)

    RATING_CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    walk_rating = models.IntegerField(blank=True, choices=RATING_CHOICES)

    date_posted = models.DateTimeField(auto_now_add=True)
    approve_count = models.IntegerField(default=0)
    disapprove_count = models.IntegerField(default=0)


# class Comment(models.Model):
#     # comment ID will be automatically created
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     on_review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     body = models.TextField(max_length=3000)
#     date_posted = models.DateTimeField(auto_now_add=True)
#     approve_count = models.IntegerField(default=0)
#     disapprove_count = models.IntegerField(default=0)
#     # photo = models.ImageField(default=None, height_field=768, width_field=1024)