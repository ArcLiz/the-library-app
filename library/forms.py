from django import forms
from .models import Book, Genre
from django.contrib.admin import widgets


class BookForm(forms.ModelForm):
    """ Form to add a book """

    class Meta:
        model = Book
        fields = ['title', 'author', 'series', 'num_in_series', 'genres', 'isbn',
                  'cover', 'book_type', 'read', 'review', 'rating', 'description', 'comments']

        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'series': 'Book Series',
            'num_in_series': 'Book # in Series',
            'genres': 'Genres',
            'isbn': 'ISBN(13)',
            'cover': 'Cover Image',
            'book_type': 'Type of Book',
            'read': 'Read',
            'review': 'Book Review',
            'rating': 'Rating',
            'description': 'Book Description',
            'comments': 'Other Comments'
        }


class QuickForm(forms.ModelForm):
    """ Form to add necessary book information only """

    class Meta:
        model = Book
        fields = ['title', 'author', 'isbn', 'genres', 'cover', 'book_type']

        labels = {
            'title': 'Book Title',
            'author': 'Author',
            'isbn': 'ISBN(13)',
            'genres': 'Genres',
            'cover': 'Cover Image',
            'book_type': 'Type of Book'
        }


class CSVUploadForm(forms.Form):
    csv_file = forms.FileField()
