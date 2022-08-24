from django.urls import path
from . import views


urlpatterns = [
    path('rent_book/<str:pk>', views.rentBook, name='rent-book'),
    path('return_book/<str:pk>', views.returnBook, name='return-book'),
    path('rent_history/', views.returnHistory, name='return-history'),
    path('rented', views.rented, name='rented')
]
