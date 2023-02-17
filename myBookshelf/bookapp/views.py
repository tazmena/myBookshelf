from django.shortcuts import render

#from bookapp.forms import SignUpForm, LogInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
#from bookapp.models import User
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed, HttpRequest


def loginUser(request: HttpRequest) -> JsonResponse:
    form = LogInForm()
    return render(request, 'bookapp/login.html', {'form':form})

def signup(request: HttpRequest) -> JsonResponse:
    form = SignUpForm()
    return render(request, 'bookapp/signup.html', {'form': form})
