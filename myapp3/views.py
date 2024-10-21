from django.shortcuts import render
from .forms import CreateBookForm, UpdateBookForm
from .models import Book
from django.http import HttpResponseRedirect

# View to handle form submission and save data to the Book model
from django.shortcuts import render, redirect
from .forms import CreateBookForm
from .models import Book
from django.shortcuts import render

def home(request):
    return render(request, 'myapp3/home.html')

# Create a new book
def create_book(request):
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            # Manually create and save a Book instance
            Book.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author']
            )
            return redirect('success')  # Redirect to the success page
    else:
        form = CreateBookForm()
    return render(request, 'myapp3/createbook.html', {'form': form})

from django.shortcuts import get_object_or_404

def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = CreateBookForm(request.POST)
        if form.is_valid():
            # Update the book instance
            book.title = form.cleaned_data['title']
            book.author = form.cleaned_data['author']
            book.save()
            return redirect('book_list')
    else:
        # Populate the form with the current book data
        form = CreateBookForm(initial={'title': book.title, 'author': book.author})
    return render(request, 'myapp3/updatebook.html', {'form': form, 'book': book})
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'myapp3/deletebook.html', {'book': book})
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp3/book_list.html', {'books': books})


def success(request):
    return render(request, 'myapp3/success.html')