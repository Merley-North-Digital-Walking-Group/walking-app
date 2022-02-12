from django.db import models

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=200)
    group_description = models.TextField()
    # group_photo = models.ImageField(default=None, height_field=768, width_field=1024)
    meeting_day = models.CharField(max_length=50)
    meeting_time = models.DateTimeField()
    meetup_link = models.CharField(max_length=300)

    def __str__(self):
        return self.group_name
    


 