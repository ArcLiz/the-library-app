from django.contrib import admin
from .models import Book, Genre

# Register your models here.


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'display_genres',
        'isbn',
        'cover',
        'book_type',
        'user',
        'read',
        'review',
        'rating'
    )

    def display_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])
