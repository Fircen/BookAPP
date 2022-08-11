from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('book/',views.book, name="book"),
    path('add_book/',views.addBook, name="addBook"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutPage, name="logout"),
    path('register/',views.registerUser, name="register")          
]