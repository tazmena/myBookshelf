from django.contrib import admin

# Register your models here.

from .models import User
from .models import Book
from .models import UserPreference

admin.site.register(Book)
admin.site.register(User)
admin.site.register(UserPreference)