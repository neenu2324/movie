# Generated by Django 5.0.1 on 2024-03-25 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0014_remove_movie_year_movie_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='date',
            new_name='year',
        ),
    ]
