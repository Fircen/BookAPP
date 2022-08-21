from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add_book/', views.addBook, name="add-Book"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('register/', views.registerUser, name="register"),
    path('searchbook', views.searchBook, name="search"),
    path('my_book/', views.myBook, name="my-book"),
    path('books/', views.books, name='books'),
    path('rent_book/<str:pk>', views.rentBook, name='rent-book'),
    path('return_book/<str:pk>', views.returnBook, name='return-book'),
    path('rent_history/', views.returnHistory, name='return-history'),
    path('book_info/<int:pk>', views.bookInfo, name='book-info'),
    path('edit_book/<int:pk>', views.editBook, name="edit-book"),
    path('rented', views.rented, name='rented')

]
