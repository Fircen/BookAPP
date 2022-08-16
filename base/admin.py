from django.contrib import admin

# Register your models here.
from .models import Book, Returns, rents

admin.site.register(Book)
admin.site.register(rents)
admin.site.register(Returns)