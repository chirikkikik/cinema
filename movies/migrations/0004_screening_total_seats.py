# Generated by Django 5.1.2 on 2025-01-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_poster'),
    ]

    operations = [
        migrations.AddField(
            model_name='screening',
            name='total_seats',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
