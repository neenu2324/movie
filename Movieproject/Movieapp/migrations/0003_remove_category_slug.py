# Generated by Django 5.0.1 on 2024-03-29 04:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0002_movie_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug',
        ),
    ]