import django_tables2 as tables
from .models import Book


class BookTable(tables.Table):
    """ The library view """
    title = tables.LinkColumn(
        'book_detail', args=[tables.A('pk')], verbose_name="book title")
    author = tables.Column(verbose_name="author")
    genres = tables.Column(verbose_name="genres")
    book_type = tables.Column(verbose_name="book type")
    comments = tables.Column(verbose_name="comments")
    read = tables.BooleanColumn(verbose_name="read")
    edit = tables.TemplateColumn(
        '<a href="#"><i class="fa-solid fa-pen-to-square"></i></a>', verbose_name="edit")
    delete = tables.TemplateColumn(
        '<a href="#"><i class="fa-solid fa-trash"></i></a>', verbose_name="delete")

    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap5.html"
        fields = ('title', 'author', 'genres', 'book_type', 'comments', 'read')
