# Generated by Django 5.1.2 on 2024-12-24 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='screening',
            old_name='start_at',
            new_name='start_time',
        ),
    ]
