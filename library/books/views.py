#All views here
from django.shortcuts import render,get_object_or_404,redirect
from .models import Book
from .forms import BookForm
# Create your views here.
def book_list(request):
    books = Book.objects.all().order_by("-added")
    read_count = books.filter(read=True).count() 
    return render(request, "books/book_list.html", {"books": books, "page_title": "All Books", "read_count": read_count})

def read_books(request):
    books = Book.objects.filter(read=True)
    read_count = books.count()
    return render(request, "books/book_list.html", {"books": books, "page_title": "Read Books", "read_count": read_count})

def books_by_author(request, name):
    books = Book.objects.filter(author=name)
    read_count = books.filter(read=True).count()
    return render(request, "books/book_list.html", {"books": books, "page_title": f"Books by {name}", "read_count": read_count})

def book_detail(request,pk):
    book = get_object_or_404(Book,pk=pk)
    return render(request,"books/book_detail.html",{"book":book})

def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()

    return render(request,"books/book_form.html",{"form":form,"page_title":"Add Book"})

def edit_book(request,pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail',pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form, "page_title": "Edit Book"})

def delete_book(request,pk):
    book = get_object_or_404(Book,pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect('book_list')

    return render(request,"books/book_confirm_delete.html",{"book":book})