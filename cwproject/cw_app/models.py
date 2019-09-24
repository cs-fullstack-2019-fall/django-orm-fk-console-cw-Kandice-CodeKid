from django.db import models

# Create your models here.
from django.db.models import CASCADE
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

class Post(models.Model):
    title=models.CharField(max_length=200)
    content=models.CharField(max_length=200)
    date_posted=models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author,on_delete=CASCADE)

    def __str__(self):
        return self.title