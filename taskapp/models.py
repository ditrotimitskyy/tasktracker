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
    


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name="comments", null=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    comment_pic = models.ImageField(upload_to="comment_pics/", null=True, blank=True)