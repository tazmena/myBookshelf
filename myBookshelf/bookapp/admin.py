from django.contrib import admin

# Register your models here.

from .models import User
from .models import Book

admin.site.register(Book)
admin.site.register(User)