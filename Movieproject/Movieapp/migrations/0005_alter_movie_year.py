# Generated by Django 5.0.1 on 2024-03-29 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movieapp', '0004_remove_category_des_remove_category_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
