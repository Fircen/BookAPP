from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Book, Returns, Rents
from .forms import BookForm, NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from dateutil.relativedelta import relativedelta
from datetime import date
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'base/home.html')


def books(request):
    book = Book.objects.all()
    context = {'books': book}
    return render(request, 'base/book.html', context)


def searchBook(request):
    if request.method == 'POST':
        rentBook(request)
    if request.method == 'GET':
        q = request.GET.get('q')
        book = Book.objects.filter(
            Q(title__icontains=q) | Q(author__icontains=q))
        return render(request, 'base/book.html', {'books': book})


@login_required(login_url='/login')
def myBook(request):
    rent = Rents.objects.filter(user=request.user.id)
    return render(request, 'base/my_book.html', {'rents': rent})


@login_required(login_url='/login')
def addBook(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'base/add_book.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password dont match')

    return render(request, 'base/login.html')


@login_required(login_url='/login')
def logoutPage(request):
    logout(request)
    return redirect('home')


def registerUser(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(
            request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="base/register.html")


@login_required(login_url='/login')
def rentBook(request, pk):
    selectBook = Book.objects.get(id=pk)
    if request.method == "POST":
        currentUser = request.user
        date_r = date.today() + relativedelta(weeks=+3)
        if selectBook.free:
            Rents.objects.create(
                user=currentUser, book=selectBook, return_date=date_r)
            selectBook.free = 0
            selectBook.save(update_fields=['free'])
            return redirect('my-book')
        else:
            messages.error(request, "Book is already taken")
    return render(request, 'base/add_rent.html', {'obj': selectBook})


@login_required(login_url='/login')
def returnBook(request, pk):
    selectBook = Book.objects.get(id=pk)
    selectRent = Rents.objects.get(book=pk)
    if request.method == "POST":
        if selectBook.free == 0:
            currentUser = request.user
            Returns.objects.create(user=currentUser, book=selectBook)
            selectBook.free = 1
            selectBook.save(update_fields=['free'])
            selectRent.delete()
            return redirect('my-book')
    return render(request, 'base/add_return.html', {'obj': selectBook})


@login_required(login_url='/login')
def returnHistory(request):
    Return = Returns.objects.filter(user=request.user.id)
    return render(request, 'base/rent_history.html', {'retruns': Return})
