from email import message
from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def book(request):
    book = Book.objects.all()
    context = {'books' : book}
    return render(request, 'base/book.html', context)

def addBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/add_book.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            message.error(request, 'User does not exist')

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             message.error(request, 'Username or password dont match')

    context={}
    return render(request, 'base/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')