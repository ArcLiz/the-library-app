import csv
from csv import DictReader
from io import TextIOWrapper
from typing import Any, Dict
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from django.db.models import Q

from users.models import Profile
from .models import Book, Genre
from .tables import BookTable
from .forms import BookForm, QuickForm, CSVUploadForm


# Create your views here.


class AddBook(CreateView):
    """ Add book """
    template_name = 'library/add_book.html'
    model = Book
    form_class = BookForm
    success_url = '/library/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddBook, self).form_valid(form)


class QuickAdd(CreateView):
    """ Add book """
    template_name = 'library/quick_add.html'
    model = Book
    form_class = QuickForm
    success_url = '/library/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuickAdd, self).form_valid(form)


class EditBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/edit_book.html'
    success_url = '/library'

    def get_object(self, queryset=None):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Book, pk=pk)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeleteBook(DeleteView):
    """ Delete Book View"""
    model = Book
    success_url = '/library/'
    template_name = 'library/delete_book.html'


class MyLibrary(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'library/library.html'
    context_object_name = 'books'
    paginate_by = 20

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q')
        # Check if the reset parameter is present
        reset_sorting = self.request.GET.get('reset_sorting')

        queryset = Book.objects.filter(user=user)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(author__icontains=query)
            )

        if reset_sorting:
            # Replace 'pk' with your default sorting criteria
            queryset = queryset.order_by('pk')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the total count of books
        total_books_count = Book.objects.filter(user=self.request.user).count()
        context['total_books_count'] = total_books_count

        return context


class UserLibrary(SingleTableView):
    model = Book
    table_class = BookTable
    template_name = 'library/user_library.html'
    context_object_name = 'books'
    paginate_by = 20

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        queryset = Book.objects.filter(user=user)

        query = self.request.GET.get('q')
        reset_sorting = self.request.GET.get('reset_sorting')

        if query:
            queryset = self.filter_queryset(queryset, query)

        if reset_sorting:
            # Replace 'pk' with your default sorting criteria
            queryset = queryset.order_by('pk')

        return queryset

    def filter_queryset(self, queryset, query):
        return queryset.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['user_id']
        user = get_object_or_404(User, id=user_id)
        profile = Profile.objects.get(user=user)

        total_books_count = Book.objects.filter(user=profile.user).count()

        context['total_books_count'] = total_books_count
        context['profile'] = profile
        return context


def book_details(request, pk):
    """ View for the details of the book """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


@login_required
def upload_csv(request):
    privacy_form = None

    if request.method == "POST":
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            user = request.user

            try:
                csv_text = TextIOWrapper(csv_file.file, encoding='utf-8')
                reader = DictReader(csv_text)

                for row in reader:
                    title = row['title']
                    author = row['author']
                    comments = row['comments']

                    description = row.get('description', '')
                    if len(description) > 500:
                        truncated_description = description[:500]
                    else:
                        truncated_description = description

                    combined_data = f"{truncated_description} <br><br>Book published in {row['published']}. <br>The book length is: {row['length']}"

                    # Create and save Book object
                    book = Book(title=title, author=author,
                                comments=comments, description=combined_data, user=user)
                    book.save()

                    genre_name = row['genres'].strip()
                    genre, created = Genre.objects.get_or_create(
                        name=genre_name)
                    book.genres.add(genre)

                return render(request, 'library.html', {'message': 'CSV data imported successfully.'})
            except Exception as e:
                return render(request, 'error.html', {'error_message': str(e)})

    else:
        form = CSVUploadForm()

    return render(request, 'settings.html', {'form': form})
