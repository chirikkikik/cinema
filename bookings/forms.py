from django import forms
from .models import Booking, Ticket

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'screening', 'tickets_booked', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tickets_booked'].queryset = Ticket.objects.filter(is_booked=False)
