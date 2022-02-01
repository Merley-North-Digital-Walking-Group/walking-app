from django.db import models
from geoposition.fields import GeopositionField
from PIL import Image

# Create your models here.

class Walk(models.Model):
    # walk ID will be automatically generated
    walk_name = models.CharField(max_length=100)
    map_coordinates = GeopositionField()
    walk_length = models.DecimalField(max_digits=4, decimal_places=2)
    elevation = models.IntegerField     # Ideally this will be grabbed from the highest point on Google Maps
    step_count = models.IntegerField()
    parking = models.BooleanField()
    wheelchair_access = models.BooleanField()
    toilet = models.BooleanField()
    cafe = models.BooleanField()
    rest_area = models.BooleanField()
    scenic_spot = models.BooleanField()
    dog_bin = models.BooleanField()
    rating = models.IntegerField()
    photo = models.ImageField(upload_to=None, height_field=768, width_field=1024)
    # reviews = need to connect via review IDs