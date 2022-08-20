from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    descritpion = models.CharField(max_length=600)
    free = models.BooleanField(null=True, default='True')

    def __str__(self):
        return self.title


class rents(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rent_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s'(self.user.username, self.book.title)


class Returns(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s %s'(self.user.username, self.book.title)
