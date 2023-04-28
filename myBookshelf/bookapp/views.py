import numpy as np
import pandas as pd
from django.shortcuts import render
from bookapp.forms import SignUpForm, LogInForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from bookapp.models import User
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed, HttpRequest
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer


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
    #del request.session
    return HttpResponseRedirect('http://localhost:8000')

def contentRec(request: HttpRequest) -> JsonResponse:
    df = pd.read_csv('contentbased.csv', encoding='unicode_escape', error_bad_lines = False)
    columns = ['description','genres']
    df['combined_features']=combine_features(df)
    cm = CountVectorizer().fit_transform(df['combined_features'])
    cs = cosine_similarity(cm)
    Title = df['title'][0]
    book_id = df[df.title == Title]['id'].values[0]
    scores = list(enumerate(cs[book_id]))
    sortedScores = sorted(scores, key=lambda x:x[1], reverse = True) #highest score at the top
    sortedScores = sortedScores[1:] #everything after the book itself
    k = 0
    recs = []
    print("Your 5 recommendations for " + Title + " are: \n")
    for book in sortedScores:
        bookTitle = df[df.id == book[0]]['title'].values[0]
        recs.append(bookTitle)
        k+=1
        if k >= 5:
            break
    return JsonResponse({'recs' : recs }, status=200)

def combine_features(data):
  features = []
  for i in range(0, data.shape[0]):
    print(data.shape[0])
    features.append(str(data['description'][i])+data['genres'][i])
  return features

