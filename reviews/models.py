from datetime import date
from statistics import mode
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
# from django.contrib.auth.models import User


class Review(models.Model):
    # review ID will be automatically created
    # author = need to connect to user via user/walker ID
    # walk_ID = need to connect to the walk via walk ID
    walk_rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=3000)
    date_posted = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default=None, height_field=768, width_field=1024)
    approve_count = models.IntegerField(default=0)
    disapprove_count = models.IntegerField(default=0)


class Comment(models.Model):
    # comment ID will be automatically created
    # author = pulled in from walker ID
    # on_review = pulled in from review ID
    content = models.TextField(max_length=3000)
    date_posted = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default=None, height_field=768, width_field=1024)
    approve_count = models.IntegerField(default=0)
    disapprove_count = models.IntegerField(default=0)