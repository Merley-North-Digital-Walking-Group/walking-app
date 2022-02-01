from django.db import models

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=200)
    group_description = models.TextField()
    #group_photo = models.ImageField()
    meeting_day = models.CharField(max_length=50)
    meeting_time = models.DateTimeField()
    meetup_link = models.CharField(max_length=300)
    #members_list = ForeignKey link to user ids 