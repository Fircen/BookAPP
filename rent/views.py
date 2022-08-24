from django.shortcuts import render
from books.models import Book
from .models import Rents, Returns
from dateutil.relativedelta import relativedelta
from datetime import date
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages


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
    return render(request, 'rent/add_rent.html', {'obj': selectBook})


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
    return render(request, 'rent/add_return.html', {'obj': selectBook})


@login_required(login_url='/login')
def returnHistory(request):
    Return = Returns.objects.filter(user=request.user.id)
    return render(request, 'rent/rent_history.html', {'retruns': Return})


@login_required(login_url='/login')
def rented(request):
    Rent = Rents.objects.all()
    return render(request, 'rent/rented.html', {'rents': Rent})
