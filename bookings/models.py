from django.db import models
from movies.models import Screening, Seat
from django.contrib.auth.models import User

     
class Ticket(models.Model):
    screening = models.ForeignKey(Screening,  on_delete = models.CASCADE, related_name='tickets')
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)
    seat = models.ForeignKey(Seat, default=None , on_delete=models.CASCADE, blank = False, related_name='tickets')
    is_booked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        db_table = 'Tickets'
        

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = None, related_name='bookings')
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE, related_name='bookings')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)
    tickets = models.ManyToManyField(Ticket, related_name='bookings')
    is_paid = models.BooleanField(default=False)
    
    def total_cost(self):
        return sum(ticket.price for ticket in self.tickets.all())
    
    def __str__(self):
        return f"{self.username} - {self.screening.date}"
    
    class Meta:
        db_table = 'Bookings'
    