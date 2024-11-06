from django.db import models
from movies.models import Screening, Seat
from customers.models import Customer

class Booking(models.Model):
    screening = models.ForeignKey(Screening, on_delete = models.CASCADE, default=None, related_name='bookings')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None, related_name='bookings')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0, null=False)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, blank=False, related_name='bookings')
    card_number = models.CharField(max_length=20, default = 0, null=False)
    name_on_card = models.CharField(max_length=20, default = (""), blank = False)
    
    class Meta:
        db_table = 'Bookings'
        
        
class Ticket(models.Model):
    booking = models.ForeignKey(Booking, on_delete = models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    class Meta:
        db_table = 'Tickets'
