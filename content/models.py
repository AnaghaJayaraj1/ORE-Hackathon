from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    name = models.CharField(max_length=100, default="helo")
    title = models.CharField(max_length=100)
    content = models.TextField()
    password = models.CharField(max_length=32, default="12345")
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
# Create your models here.