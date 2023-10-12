from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableView

from django.db.models import Q

from .models import Book
from .tables import BookTable
from .forms import BookForm, QuickForm


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
    """ User Library """
    model = Book
    table = BookTable
    template_name = 'library/library.html'
    context_object_name = 'books'

    def get_queryset(self):
        user = self.request.user
        query = self.request.GET.get('q')

        queryset = Book.objects.filter(user=user)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(
                    author__icontains=query) | Q(series__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unread'] = context['books'].filter(read=False).count()
        return context


def book_details(request, pk):
    """ View for the details of the book """
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})
