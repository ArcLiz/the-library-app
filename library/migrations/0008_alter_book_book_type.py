# Generated by Django 3.2.21 on 2023-11-09 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_book_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('Ebook', 'Ebook'), ('Audiobook', 'Audiobook'), ('Hardcover', 'Hardcover'), ('Paperback', 'Paperback')], max_length=20),
        ),
    ]
