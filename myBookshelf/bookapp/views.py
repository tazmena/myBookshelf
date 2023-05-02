from django.shortcuts import render
from bookapp.forms import SignUpForm, LogInForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from bookapp.models import User, Book, UserPreference, UserToRead, Rating
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed, HttpRequest
import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import json


def loginUser(request: HttpRequest) -> JsonResponse: #:Logs user in, Reference: code of login, signup, session and logout methods written by myself for web programming module
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(data=request.POST)
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(request, username=uname, password=pword) #Makes use of Django authentification framework to check the username and password against the database
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('http://localhost:5173')
        else:
            messages.error(request,'Login failed. Please try again')
    return render(request, 'bookapp/login.html', {'form':form})

def signup(request: HttpRequest) -> JsonResponse: #Signs the user up, creates a new user object

    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        if form.is_valid(): #Checks that all the inputs are correctly input (such as no empty fields)
            user = User.objects.create_user(email=email,username=username,password=password,first_name=first_name,last_name=last_name) #Create user built in Django method used to create the user in the database and correctly hash the password, the log in will not work otherwise
            user.save()
            form = SignUpForm() #Re renders the sign up form
            messages.success(request, 'Account created successfully')
        else:
            messages.error(request, 'Account not created, try again.')

    return render(request, 'bookapp/signup.html', {'form': form})

def session_api(request : HttpRequest) -> JsonResponse: #Sends userId detected in the current session to frontend
    form = LogInForm()
    if request.method == "GET":
        try:
            return JsonResponse( { 'user_id' : request.session.__getitem__("_auth_user_id") } , safe=False ) #eEference - https://stackoverflow.com/questions/8000040/how-to-get-logged-in-users-uid-from-session-in-django
        except:
            return HttpResponseNotAllowed
        
def getUserObj(request : HttpRequest, user_id : int) -> JsonResponse: #Converts userid to user object
    userobj = get_object_or_404(User, id=user_id) #Finds an object that matches the input argument (eg. id= given user id) or returns 404 error
    return JsonResponse({'user': userobj.to_dict(),}, status=200) #Returns this object as json, object is converted to dictionary
        
def logOutUser(request : HttpRequest, user_id : int) -> HttpResponseRedirect: #Logs the user out
    #logout(request)
    del request.session["user_id"] #Deletes the sessionid, ending the session Reference - https://docs.djangoproject.com/en/4.2/topics/http/sessions/
    return HttpResponseRedirect('http://localhost:8000') #Returns user back to backend localhost

def getBookIds(user_id): #To get all the bookIds for the books the user chose in the quiz
    user = User.objects.get(id=user_id)
    userpreference = UserPreference.objects.get(User=user)
    listofbooks = userpreference.likedbooks.split(',') #Splits the string by commas, returns an array
    bookids = []
    for bookname in listofbooks:
        book = Book.objects.get(title=bookname)
        bookids.append(book.id)
    return bookids

def contentRec(request : HttpRequest, user_id : int) -> JsonResponse: #Reference for recommendation: https://www.youtube.com/watch?v=xySjbVUgAwU&t=994s
    user = User.objects.get(id=user_id)
    userpreference = UserPreference.objects.get(user=user)
    bookids = userpreference.likedbooks.split(',')
    bookids2 = [] #Gets a list of all the books for a user in user preference, these are the books they selected in quiz
    for i in range(len(bookids)):
        if bookids[i] != "":
            bookids2.append(int(bookids[i])-1)


    df = pd.read_csv('content.csv', encoding='unicode_escape') #Reads the csv file
    columns = ['description','genres']
    df['combined_features']=combine_features(df) #Calls combine feature function
    cm = CountVectorizer().fit_transform(df['combined_features'])
    cs = cosine_similarity(cm)

    #bookids = [1284-1,212,836,2475,1]
    allrecs = []

    for bookid in bookids2:
        Title = df['title'][bookid]
        book_id = df[df.title == Title]['id'].values[0]
        scores = list(enumerate(cs[book_id]))
        sortedScores = sorted(scores, key=lambda x:x[1], reverse = True) #highest score at the top
        sortedScores = sortedScores[1:] #everything before and after the book itself
        k = 0
        recs = []
        print("Your 5 recommendations for " + Title + " are: \n")
        for book in sortedScores:
            bookTitle = df[df.id == book[0]]['title'].values[0]
            allrecs.append(bookTitle)
            k+=1
            if k >= 2:
                break
    print("Bookss",bookids2)
    print(user_id)
    allrecsobj = [] #recommendations stored as Book object
    for i in range(len(allrecs)):
        allrecsobj.append(get_object_or_404(Book, title=allrecs[i]))
    return JsonResponse({'allrecs' : [rec.to_dict() for rec in allrecsobj]}, status=200)

def combine_features(data):
  features = []
  for i in range(0, data.shape[0]):
    print(data.shape[0])
    features.append(str(data['description'][i])+data['genres'][i])
  return features

def getBookData(request : HttpRequest) -> JsonResponse: #Gets all the books in the database and returns a Json with a dictionary for each book
    if request.method == "GET":
        allBooks = Book.objects.all() #Queryset of all books in Book model, Reference: https://docs.djangoproject.com/en/4.2/topics/db/queries/
        return JsonResponse({'books': [book.to_dict() for book in allBooks],}, status=200) #Dictionary of all books and their info

def getBookId(request : HttpRequest, book_title : str) -> JsonResponse: #Takes in a book title and returns book id
    if request.method == "GET":
        book = get_object_or_404(Book, title=book_title)
        bookid = book.id
        return JsonResponse({'bookId': bookid,}, status=200)  
    
def getToRead(request : HttpRequest, user_id : int) -> JsonResponse:
    if request.method == "GET":
        user = get_object_or_404(User, id=user_id)
        allusers = UserToRead.objects.all()
        for item in allusers:
            chosenuser = item.user
            if chosenuser.id == user.id:
                userbooks = item.bookstoread
                books = userbooks.split(',')
                allbooks =[]
                allbooksobj = []
                for i in range(len(books)-1):
                    allbooks.append(books[i])
                for k in range(len(allbooks)):
                    allbooksobj.append(get_object_or_404(Book, id=allbooks[k]))
                return JsonResponse({'userbooks': [book.to_dict() for book in allbooksobj]}, status=200)
        return JsonResponse({'userbooks': ''}, status=200)

def getCompleted(request : HttpRequest, user_id : int) -> JsonResponse:
    if request.method == "GET":
        user = get_object_or_404(User, id=user_id)
        allusers = UserToRead.objects.all()
        for item in allusers:
            chosenuser = item.user
            if chosenuser.id == user.id:
                userbooks = item.bookscompleted
                books = userbooks.split(',')
                allbooks =[]
                allbooksobj = []
                for i in range(len(books)-1):
                    allbooks.append(books[i])
                for k in range(len(allbooks)):
                    allbooksobj.append(get_object_or_404(Book, id=allbooks[k]))
                return JsonResponse({'userbooks': [book.to_dict() for book in allbooksobj]}, status=200)
        return JsonResponse({'userbooks': ''}, status=200)      

@csrf_exempt
def addBook(request : HttpRequest) -> JsonResponse: #Adds book from quiz results to UserPreference object for current user
    if request.method == "POST":
        res = json.loads(request.body.decode('utf-8')) #Loads body
        #book = get_object_or_404(Book, id=book_id)
        currentuser = get_object_or_404(User, id=res['user_id'])
        bookid = str(res['book_id'])
        allusers = UserPreference.objects.all() #Gets all the current users who have previously answered the quiz

        for item in allusers: #Check all users, see if any user name matches current user's username, if yes, append string of selected book to previously selected books.
            chosenuser = item.user
            if chosenuser.username == currentuser.username:
                item.likedbooks += (bookid+",")
                item.save()
                return JsonResponse({'success':"succss"},status=200)
            
        userresult = UserPreference.objects.create() #If for loop does not find user, a new userpreference object is created to track their quiz results.
        userresult.user = currentuser
        userresult.likedbooks += (bookid+",")
        userresult.save()
        return JsonResponse({'success':"success"},status=200)

@csrf_exempt  
def addBookToRead(request : HttpRequest) -> JsonResponse: #Adds selected book to "to read" so that user can see it in the home page
    if request.method == "POST":
        res = json.loads(request.body.decode('utf-8')) #Loads body
        #book = get_object_or_404(Book, id=book_id)
        currentuser = get_object_or_404(User, id=res['user_id'])
        bookid = str(res['book_id'])
        allusers = UserToRead.objects.all()

        for item in allusers:
            chosenuser = item.user
            if chosenuser.username == currentuser.username:
                item.bookstoread += (bookid+",")
                item.save()
                return JsonResponse({'success':"succss"},status=200)
            
        userresult = UserToRead.objects.create()
        userresult.user = currentuser
        userresult.bookstoread += (bookid+",")
        userresult.save()
        return JsonResponse({'success':"success"},status=200)

@csrf_exempt    
def moveToComplete(request : HttpRequest) -> JsonResponse: #Deletes book from to read, and appends to completed books
    if request.method == "PUT":
        res = json.loads(request.body.decode('utf-8')) #Loads body
        currentuser = get_object_or_404(User, id=res['user_id'])
        bookid = str(res['book_id'])
        alltrackedbooks = UserToRead.objects.all()

        for item in alltrackedbooks:
            chosenuser = item.user
            if chosenuser.username == currentuser.username:
                toreadbooks = item.bookstoread.split(",")
                for i in range(len(toreadbooks)-1): #Minus one as toreadbooks always returns an empty value at the end
                    if str(toreadbooks[i]) == bookid: #Finds book in to read
                        item.bookscompleted += (bookid+",") #Adds book to completed
                        #stringtoreplace = bookid+","
                        newbooks = item.bookstoread.replace((bookid+","),"") #Deletes book from to read
                        item.bookstoread = newbooks
                        item.save()
        return JsonResponse({'success':"success"},status=200)

@csrf_exempt #To allow for post requests to be sent to backend from frontend   
def resetQuiz(request: HttpRequest) -> JsonResponse: #To reset quiz so user can update their preferences
    res = json.loads(request.body.decode('utf-8')) #Loads body
    user = get_object_or_404(User, id=res['user_id'])
    get_object_or_404(UserPreference, user=user).delete() #Deletes userpreference object for user so that they can retake quiz
    return JsonResponse({'deletesuccess':'deletesuccess'},status=200)

def getQuizResults(request:HttpRequest, user_id:int) -> JsonResponse: 
    user = get_object_or_404(User, id=user_id)
    preference = get_object_or_404(UserPreference, user=user)
    books = preference.likedbooks.split(",")
    booksobj = []

    for i in (range(len(books)-1)):
        booksobj.append(get_object_or_404(Book, id=books[i]))
    return JsonResponse({'books':[book.to_dict() for book in booksobj]},status=200)

@csrf_exempt    
def saveRating(request: HttpRequest) -> JsonResponse: #Save user rating, taking in the book, and its corresponding rating.
    res = json.loads(request.body.decode('utf-8'))
    currentuser = get_object_or_404(User, id=res['user_id'])
    book = get_object_or_404(Book, title=res['bookTitle'])
    bookid = str(book.id)
    ratingval = str(res['ratingVal'])
    allusers = Rating.objects.all()

    for item in allusers:
        chosenuser = item.user
        if chosenuser.username == currentuser.username:
            item.books += (bookid+",")
            item.ratings += (ratingval+",")
            item.save()
            return JsonResponse({'success':"succss"},status=200)
            
    userresult = Rating.objects.create()
    userresult.user = currentuser
    userresult.books += (bookid+",")
    userresult.ratings += (ratingval+",")
    userresult.save()
    return JsonResponse({'success':"success"},status=200)

