from itertools import count
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from books.models import Book
from rent.models import Rents
from django.db.models import Count


def home(request):
    book = Book.objects.annotate(num_rent=Count(
        'returns')).order_by('-num_rent')[:5]
    return render(request, 'base/home.html', {'books': book})


@login_required(login_url='/login')
def myBook(request):
    rent = Rents.objects.filter(user=request.user.id)
    return render(request, 'base/my.html', {'rents': rent})


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
    return render(request, "base/register.html",  {'register_form': form})
