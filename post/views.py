from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

# built in django user
from django.contrib.auth.models import User

# for user login
from django.contrib.auth import authenticate, login, logout

# built in function for sending messages in django
from django.contrib import messages

# check to make the user is login before acccessing the view
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    posts = Post.objects.all().values()
    page_name = "Home page"
    return render(request, "home.html", {'posts': posts, 'page_name':page_name})

@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('Aname')
        if title and content and author:
            post = Post.objects.create(title=title, content=content,author=author, published_date=timezone.now())
            post.save()
            return redirect('home')
        
    return render(request, "add_post.html")

def register(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        first_name= request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password= request.POST.get('password')
        if username and first_name and last_name and email and password:
            user = User.objects.create(username=username, first_name=first_name,email=email, password=password)
            user.set_password(password)
            user.save()
            
            print(f"Hashed password for user {username}: {user.password}")
            return redirect('home')
        
    return render(request, "register.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('register')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    print("User request:",request.user)
    return render(request, 'dashboard.html')


from .send_email import send_email
from django.http import HttpResponse

def sender_email(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        print(f"Hi {firstname}, with subject: {subject} has the message {message}")
        try:
            subject = subject
            body = message
            to_email = email
            from_email = 'abibangbrandon855@outlook.com'
            password = ''
            send_email(subject, body, to_email, from_email, password)
            return HttpResponse(f"Email sent successfully to {email} check your inbox")
        except Exception as e:
            return HttpResponse(f"Failed to send email: {e}")
    return render(request, 'contact.html')

















# Create your views here.
