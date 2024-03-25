# Generated by Django 5.0.1 on 2024-03-25 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0013_alter_movie_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
        migrations.AddField(
            model_name='movie',
            name='date',
            field=models.DateField(default=''),
            preserve_default=False,
        ),
    ]