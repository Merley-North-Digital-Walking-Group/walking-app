from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class App_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    group = models.ManyToManyField('groups.Group')
    #walker id is automatically generated
    #user_type = models.CharField(max_length=20)
    #name_first = models.CharField(max_length=200)
    #name_last = models.CharField(max_length=200)
    #username_handle = models.CharField(max_length=200)
    #password = models.CharField(max_length=100)
    #email = models.CharField(max_length=200)
   

    def __str__(self):
        return self.user.username