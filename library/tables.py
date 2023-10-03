import django_tables2 as tables
from .models import Book


class BookTable(tables.Table):
    """ The library view """
    title = tables.LinkColumn('book_detail', args=[tables.A('pk')])
    author = tables.Column()
    genres = tables.Column()
    book_type = tables.Column()
    comments = tables.Column()
    edit = tables.TemplateColumn(
        '<a href="#"><i class="fa-solid fa-pen-to-square"></i></a>')
    delete = tables.TemplateColumn(
        '<a href="#"><i class="fa-solid fa-trash"></i></a>')

    class Meta:
        model = Book
        template_name = "django_tables2/bootstrap.html"
