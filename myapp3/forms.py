from django import forms
from .models import Book

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']

class UpdateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author']
