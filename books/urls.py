from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.books, name='all'),
    path('all/<int:page>', views.books),
    path('add_book/', views.addBook, name="add-Book"),
    path('<int:pk>', views.bookInfo, name='book-info'),
    path('edit/<int:pk>', views.editBook, name="edit-book"),
    path('search/<int:page>', views.searchBook, name="search")
]
