from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=30)
    publisher = models.CharField(max_length=100)
    descritpion = models.CharField(max_length=600)
    free = models.BooleanField()
    def __str__(self):
        return self.title
