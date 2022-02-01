from django.db import models

# Create your models here.
class User(models.Model):
    #walker id is automatically generated
    user_type = models.CharField(max_length=20)
    name_first = models.CharField(max_length=200)
    name_last = models.CharField(max_length=200)
    username_handle = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)
    DOB = models.DateField()
    password = models.CharField(max_length=100)
    #groups = models.ForeignKey("groups", on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=200)