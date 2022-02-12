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
    location = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    group = models.ManyToManyField('groups.Group')
    

    def __str__(self):
        return self.name_first