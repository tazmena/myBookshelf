from django.urls import path
from . import views

app_name = 'bookapp'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'),
    path('user', views.session_api, name="get_userid"),
    path('logout/<int:user_id>', views.logOutUser, name='logout'),
    path('recommendations/<int:user_id>', views.contentRec, name='recommendations'),
    path('user/<int:user_id>', views.getUserObj, name="getUserObj"),
    path('searchbooks', views.getBookData, name="getBookData"),
    path('getBookId/<str:book_title>', views.getBookId, name="getBookId"),
    path('addBook/<int:user_id>/<int:book_id>', views.addBook, name="addBook"),


]
