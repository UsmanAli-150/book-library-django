from django.urls import path
from . import views

urlpatterns = [
    path('books/',views.book_list,name="book_list"),
    path('books/add/',views.create_book,name="book_create"),
    path('books/read/',views.read_books,name="book_read"),
    path('books/author/<str:name>/',views.books_by_author,name="book_by_Author"),
    path('books/<int:pk>/',views.book_detail,name="book_detail"),  
    path('books/<int:pk>/edit/',views.edit_book,name="book_edit"),
    path('books/<int:pk>/delete/',views.delete_book,name="book_delete")
]
