# Generated by Django 5.1.2 on 2024-12-16 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_booking_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='tickets_booked',
            field=models.ManyToManyField(blank=True, to='bookings.ticket'),
        ),
    ]