from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    objects = CustomUserManager()

class Task(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name='tasks')

    priorety = models.PositiveSmallIntegerField()


class CompletedTask(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    author = models.ForeignKey(User, 
                               on_delete=models.CASCADE, 
                               related_name='completed_tasks')

    priorety = models.PositiveSmallIntegerField()
