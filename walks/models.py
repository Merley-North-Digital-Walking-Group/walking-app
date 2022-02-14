# from tkinter import Image
from django.db import models

# Create your models here.

class Walk(models.Model):
    # walk ID will be automatically generated
    walk_name = models.CharField(max_length=100)
    walk_length = models.DecimalField(max_digits=4, decimal_places=2, help_text="Distance in miles")
    # elevation = models.IntegerField(default=0)     # Ideally this will be grabbed from the highest point on Google Maps
    step_count = models.IntegerField(default=None)
    parking = models.BooleanField()
    wheelchair_access = models.BooleanField()
    toilet = models.BooleanField()
    cafe = models.BooleanField()
    rest_area = models.BooleanField()
    scenic_spot = models.BooleanField()
    dog_bin = models.BooleanField()
    rating = models.IntegerField(help_text="Rating out of 5")
    lat = models.DecimalField(max_digits=9, decimal_places=6, default=50.78448)
    lng = models.DecimalField(max_digits=9, decimal_places=6, default=-1.96783)
    photo = models.ImageField(null=True, blank=True, upload_to="walks/photos/")

    # reviews = models.ManyToManyField
    # reviews = need to connect via review IDs