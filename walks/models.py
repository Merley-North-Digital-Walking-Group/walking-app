from django.db import models
# from pandas import to_timedelta

# Create your models here.

class Walk(models.Model):
    walk_name = models.CharField(max_length=100)
    walk_length = models.DecimalField(max_digits=4, decimal_places=2)
    parking = models.BooleanField()
    wheelchair_access = models.BooleanField()
    toilet = models.BooleanField()
    cafe = models.BooleanField()
    rest_area = models.BooleanField()
    scenic_spot = models.BooleanField()
    dog_bin = models.BooleanField()
    rating = models.IntegerField()
    photo = models.ImageField()
    # map_coordinates =
    # reviews = 
    # elevation =
    # step_count = 