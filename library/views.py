from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django_tables2 import SingleTableView
from .models import Book
from .forms import BookForm, QuickAdd
from .tables import BookTable

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
    form_class = QuickAdd
    success_url = '/library/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(QuickAdd, self).form_valid(form)


class MyLibrary(SingleTableView):
    """ User Library """
    model = Book
    table_class = BookTable
    template_name = 'library/library.html'


def BookDetails(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})
