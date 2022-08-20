from django.contrib import admin

# Register your models here.
from .models import Book, Returns, Rents

admin.site.register(Book)
admin.site.register(Rents)
admin.site.register(Returns)
