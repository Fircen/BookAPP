from django.contrib import admin

# Register your models here.
from .models import Book, Raiting, Returns, Rents

admin.site.register(Book)
admin.site.register(Rents)
admin.site.register(Returns)
admin.site.register(Raiting)
