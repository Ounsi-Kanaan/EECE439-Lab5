from django.urls import path
from .views import create_book, update_book, delete_book, success
from . import views
urlpatterns = [
    path('books/', views.book_list, name='book_list'), 
    path('success/', success, name='success'),
    path('create/', create_book, name='create_book'),
    path('update/<int:pk>/', update_book, name='update_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
]
