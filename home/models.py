from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class Todo(models.Model):
    title = models.CharField(max_length=250)
    details = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title