from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):

    titles = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    due_date = models.DateField(blank=True, null=True)
    