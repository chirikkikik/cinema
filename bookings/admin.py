from django.contrib import admin
from .models import Booking, Ticket

admin.site.register(Ticket)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'screening', 'is_paid', 'booking_date')
    fields = ('user', 'screening', 'tickets_booked', 'is_paid')
