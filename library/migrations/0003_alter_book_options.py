# Generated by Django 3.2.21 on 2023-10-03 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20231003_1705'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['author', 'series', 'num_in_series', 'title']},
        ),
    ]
