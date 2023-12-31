# Generated by Django 3.2.21 on 2023-10-04 09:27

from django.db import migrations
import djrichtextfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20231004_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=djrichtextfield.models.RichTextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='wishlist',
            name='list',
            field=djrichtextfield.models.RichTextField(blank=True, max_length=2500, null=True),
        ),
    ]
