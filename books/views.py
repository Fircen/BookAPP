from django.shortcuts import render
from books.models import Book
from .models import Book, Raiting
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .forms import BookForm, RateForm
from django.db.models import Q


def books(request, page):
    book = Book.objects.all()
    paginator = Paginator(book, 1)
    page_obj = paginator.get_page(page)
    page_obj.adjusted_elided_pages = paginator.get_elided_page_range(
        page)

    return render(request, 'books/all.html', {'page_obj': page_obj})


def searchBook(request, page):
    if request.method == 'GET':
        q = request.GET.get('q')
        book = Book.objects.filter(
            Q(title__icontains=q) | Q(author__icontains=q))
        paginator = Paginator(book, 5)
        page_obj = paginator.get_page(page)
        page_obj.adjusted_elided_pages = paginator.get_elided_page_range(
            page)

        return render(request, 'books/all.html', {'page_obj': page_obj, 'query': q})


@login_required(login_url='/login')
def addBook(request):
    if request.user.is_staff:
        form = BookForm()
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home')
        return render(request, 'books/add.html', {'form': form})
    return redirect('home')


def bookInfo(request, pk):
    selectBook = Book.objects.get(id=pk)
    rate = Raiting.objects.filter(book_id=pk)
    form = RateForm()
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RateForm(request.POST)
            if form.is_valid():
                f = form.save(commit=False)
                f.user = request.user
                f.book = selectBook
                f.save()
                return redirect('book-info', pk)
    else:
        redirect('login')

    return render(request, 'books/info.html', {'obj': selectBook, 'rates': rate, 'form': form})


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

        return render(request, 'books/edit.html', {'form': form})
    return redirect('home')
