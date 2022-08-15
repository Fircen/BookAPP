from django.contrib import messages
from telnetlib import AUTHENTICATION
from django.shortcuts import render, redirect
from .models import Book, rents
from .forms import BookForm, NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def books(request):
    book = Book.objects.all()
    context = {'books' : book}
    return render(request, 'base/book.html', context)

def searchbook(request):
    if request.method == 'GET':
        q=request.GET.get('q')
        book = Book.objects.filter(Q(title__icontains = q) | Q(author__icontains =q))
        
    return render(request, 'base/book.html', {'books' : book})

def mybook(request):
    book = Book.objects.filter(rents__user = request.user.id)
    rent = rents.objects.filter(user = request.user.id)
   
    context = {'books' : book, 'rents' : rent}
    return render(request, 'base/my_book.html', context)

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
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'Username or password dont match')

    context={}
    return render(request, 'base/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('home')

def registerUser(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="base/register.html", context={"register_form":form})
