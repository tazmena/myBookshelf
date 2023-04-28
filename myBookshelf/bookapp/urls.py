from django.urls import path
from . import views

app_name = 'bookapp'
urlpatterns = [
    path('', views.loginUser, name='login'),
    path('signup', views.signup, name='signup'),
    path('user', views.session_api, name="get_userid"),
    path('logout/<int:user_id>', views.logOutUser, name='logout'),
]
