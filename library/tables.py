import django_tables2 as tables
from .models import Book


class BookTable(tables.Table):
    """ Table to view all books for one user """
    title = tables.LinkColumn(
        'book_detail', args=[tables.A('pk')], verbose_name="Title")
    author = tables.Column(verbose_name="Author")
    genres = tables.Column(empty_values=(), verbose_name="Genres")

    def render_genres(self, value):
        return ', '.join([genre.name for genre in value.all()])

    book_type = tables.Column(verbose_name="Format")
    read = tables.BooleanColumn(verbose_name="Read")
    comments = tables.Column(verbose_name="Comments")

    class Meta:
        model = Book
        template_name = "library/custom_table.html"
        fields = ('title', 'author', 'genres', 'book_type', 'read', 'comments')
