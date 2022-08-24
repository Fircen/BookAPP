from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    descritpion = models.CharField(max_length=600)
    free = models.BooleanField(null=True, default='True')
    cover = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title


class Raiting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    comment = models.TextField(blank=True, null=True, max_length=300)
    rate = models.IntegerField(default=1, validators=[
        MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return str(self.pk)
