from django.contrib import admin

# Register your models here.

from .models import User
from .models import Book
from .models import UserPreference
from .models import UserToRead

admin.site.register(Book)
admin.site.register(User)
admin.site.register(UserPreference)
admin.site.register(UserToRead)
