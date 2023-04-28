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

#class UserPreference():
#    user = models.ForeignKey(User)
#    likedBooks = models.CharField()

class Book(models.Model):
    isbn = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    rating = models.FloatField()
    likedpercent = models.IntegerField()
    description = models.CharField(max_length=1000)
    pages = models.IntegerField()
    genres = models.CharField(max_length=1000)
    coverImg = models.CharField(max_length=500)

    def __str__(self):
        return self.title
