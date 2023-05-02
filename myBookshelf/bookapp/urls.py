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
    path('addBook', views.addBook, name="addBook"),
    path('addBookToRead', views.addBookToRead, name="addBookToRead"),
    path('getToRead/<int:user_id>', views.getToRead, name="getToRead"),
    path('getCompleted/<int:user_id>', views.getCompleted, name="getCompleted"),
    path('moveToComplete', views.moveToComplete, name="moveToComplete"),
    path('resetQuiz', views.resetQuiz, name="resetQuiz"),
    path('getQuizResults/<int:user_id>', views.getQuizResults, name="getQuizResults"),
    path('saveRating', views.saveRating, name="saveRating")

]
