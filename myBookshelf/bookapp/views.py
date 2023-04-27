from django.shortcuts import render
from bookapp.forms import SignUpForm, LogInForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from bookapp.models import User
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed, HttpRequest


def loginUser(request: HttpRequest) -> JsonResponse: #Code of these 3 methods written by myself for web programming module
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(data=request.POST)
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            login(request,user)
            #messages.success(request, 'Login success')
            ## return HttpResponseRedirect('http://127.0.0.1:5173')
            return HttpResponseRedirect('http://localhost:5173')
        else:
            messages.error(request,'Login failed. Please try again')
    return render(request, 'bookapp/login.html', {'form':form})

def signup(request: HttpRequest) -> JsonResponse:

    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        if form.is_valid():
            user = User.objects.create_user(email=email,username=username,password=password,first_name=first_name,last_name=last_name)
            user.save()
            form = SignUpForm()
            messages.success(request, 'Account created successfully')
        else:
            messages.error(request, 'Account not created, try again.')

    return render(request, 'bookapp/signup.html', {'form': form})

def session_api(request : HttpRequest) -> JsonResponse:
    form = LogInForm()
    if request.method == "GET":
        try:
            return JsonResponse( { 'user_id' : request.session.__getitem__("_auth_user_id") } , safe=False )
        except:
            return HttpResponseNotAllowed
        
def logOutUser(request : HttpRequest, user_id : int) -> HttpResponseRedirect:
    logout(request)
    del request.session
    HttpResponseRedirect('http://localhost:8000')
