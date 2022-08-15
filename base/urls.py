from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('add_book/',views.addBook, name="addBook"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('register/',views.registerUser, name="register"),
    path('searchbook/',views.searchbook, name="search"),
    path('my_book/',views.mybook, name="my_book"),
    path('books/', views.books, name='books')  
          
]