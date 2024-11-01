from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):

    STATUS_CHOICES = {
        "done": "Done",
        "in_prog": "In Progress",
        "on_pause": "On Pause",
    }

    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)

    status = models.CharField(choices=STATUS_CHOICES, max_length=10, default="in_prog")
    