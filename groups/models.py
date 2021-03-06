from django.db import models

# Create your models here.
class Group(models.Model):
    group_name = models.CharField(max_length=200)
    group_description = models.TextField()
    # group_photo = models.ImageField(default=None, height_field=768, width_field=1024)
    meeting_day = models.CharField(max_length=50)
    meeting_time =  models.CharField(max_length=200, default = "Meeting times may vary, please check with group")
    meetup_link = models.CharField(max_length=300, help_text="Must include 'https://www.' ")

    def __str__(self):
        return '%s %s' % (self.group_name, self.meeting_day)
    


 