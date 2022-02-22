from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class App_User(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    DOB = models.DateField()
    gender = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    group = models.ManyToManyField('groups.Group')
    
   
    def __str__(self):
        return self.user.username