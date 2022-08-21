from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Book, Returns, Rents
from .forms import BookForm, NewUserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from dateutil.relativedelta import relativedelta
from datetime import date
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


def home(request):
    book = Book.objects.all().order_by('?')[:5]
    return render(request, 'base/home.html', {'books': book})


def books(request):
    book = Book.objects.all()
    paginator = Paginator(book, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(
        page_number)

    return render(request, 'base/book.html', {'page_obj': page_obj})


def searchBook(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        book = Book.objects.filter(
            Q(title__icontains=q) | Q(author__icontains=q))

        return render(request, 'base/book.html', {'page_obj': book})


@login_required(login_url='/login')
def myBook(request):
    rent = Rents.objects.filter(user=request.user.id)
    return render(request, 'base/my_book.html', {'rents': rent})


@login_required(login_url='/login')
def addBook(request):
    if request.user.is_staff:
        form = BookForm()
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'base/add_book.html', {'form': form})
    return redirect('home')


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


def bookInfo(request, pk):
    selectBook = Book.objects.get(id=pk)
    return render(request, 'base/book_info.html', {'obj': selectBook})


@login_required(login_url='/login')
def editBook(request, pk):
    if request.user.is_staff:
        book = Book.objects.get(id=pk)
        form = BookForm(instance=book)
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES, instance=book)
            if form.is_valid():
                form.save()
                return redirect('book-info', pk)

        return render(request, 'base/edit_book.html', {'form': form})
    return redirect('home')


@login_required(login_url='/login')
def rented(request):
    Rent = Rents.objects.all()
    return render(request, 'base/rented.html', {'rents': Rent})
