# Generated by Django 3.2.21 on 2023-10-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20231004_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='amazon_wl',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='goodreads',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='storygraph',
            field=models.URLField(blank=True, null=True),
        ),
    ]
