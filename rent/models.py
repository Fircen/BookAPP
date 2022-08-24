from django.db import models
from books.models import Book
from django.contrib.auth.models import User
# Create your models here.


class Rents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Returns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s %s'(self.user.username, self.book.title)
