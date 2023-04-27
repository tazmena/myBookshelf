from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=250,unique=True)
    username = models.CharField(max_length=150,unique=True)
    password = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    newuser = models.BooleanField(default=True)
    

    def __str__(self):
        return self.username
