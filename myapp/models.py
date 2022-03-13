from django.db import models
from django.forms import IntegerField

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)
    passcode = models.CharField(max_length=100)
    def __str__(self):
        return self.name



