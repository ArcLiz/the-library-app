from django.db import models
from django.contrib.auth.models import User

from django_resized import ResizedImageField

# Create your models here.


class Genre(models.Model):
    """ A model to create the list of genres """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    """ A model to create and manage books """
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    isbn = models.CharField(max_length=13)  # Assuming ISBN-13 format
    cover = ResizedImageField(
        size=[400, None], quality=75, upload_to='books/', force_format='WEBP',
        blank=True, null=True
    )
    BOOK_TYPES = (
        ('ebook', 'Ebook'),
        ('audiobook', 'Audiobook'),
        ('hardcover', 'Hardcover'),
        ('paperback', 'Paperback'),
    )
    book_type = models.CharField(max_length=20, choices=BOOK_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    review = models.TextField(blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True, choices=[
                                 (i, i) for i in range(1, 6)])
    comments = models.CharField(max_length=200, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.book_type = self.book_type.capitalize()
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
