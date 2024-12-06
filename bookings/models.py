from django.db import models
from movies.models import Screening
from django.contrib.auth.models import User

     
class Ticket(models.Model):
    screening = models.ForeignKey(Screening,  on_delete = models.CASCADE, related_name='tickets')
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)
    seat = models.CharField(max_length=5, default = '')
    is_booked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        db_table = 'Tickets'
        

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    tickets_booked = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='booking')
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')])
    
    def total_cost(self):
        return sum(ticket.price for ticket in self.tickets.all())
    
    def cancel_booking(self):
        self.status = 'Cancelled'
        for ticket in self.tickets_booked.all():
            ticket.is_booked = False
            ticket.save()
        self.screening.available_seats += self.tickets_booked.count()
        self.screening.save()
        self.save()

    def __str__(self):
        return f"Booking for {self.user.username} at {self.screening.movie.title} on {self.screening.start_time}"

    