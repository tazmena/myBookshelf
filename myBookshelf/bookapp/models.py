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
    
    def to_dict(self):
        return {
            'email': self.email,
            'username': self.username,
            'password' : self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'newuser': self.newuser
            }
    
class UserToRead(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    bookstoread = models.CharField(max_length=1000)
    bookscompleted = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.user.username

    def to_dict(self):
        return {
            'user': self.user,
            'bookstoread' : self.bookstoread,
            'bookscompleted' : self.bookscompleted
            }

class UserPreference(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    likedbooks = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username

    def to_dict(self):
        return {
            'user': self.user,
            'likedbooks' : self.likedbooks,
            }
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    books = models.CharField(max_length=1000)
    ratings = models.CharField(max_length=1000)

    def __str__(self):
        return self.user.username

    def to_dict(self):
        return {
            'user': self.user,
            'books' : self.books,
            'ratings' : self.ratings
            }

class Book(models.Model):
    isbn = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    rating = models.FloatField()
    likedpercent = models.IntegerField()
    description = models.CharField(max_length=1000)
    pages = models.IntegerField()
    genres = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
    
    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title' : self.title,
            'author': self.author,
            'rating' : self.rating,
            'likedpercent': self.likedpercent,
            'description' : self.description,
            'pages' : self.pages,
            'genres' : self.genres,
            }
