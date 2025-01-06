from django.db import models
from movies.models import Screening
from django.contrib.auth.models import User

     
class Ticket(models.Model):
    screening = models.ForeignKey(Screening,  on_delete = models.CASCADE, related_name='tickets')
    price = models.DecimalField(max_digits=10, decimal_places=2, default = 0.0)
    seat = models.CharField(max_length=5)
    is_booked = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.seat}-{self.screening}"
    
    class Meta:
        db_table = 'Tickets'
        

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    screening = models.ForeignKey(Screening, on_delete=models.CASCADE)
    tickets_booked = models.ManyToManyField(Ticket, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)
    is_paid=models.BooleanField(default=False)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')
    
    def total_cost(self):
        return sum(ticket.price for ticket in self.tickets_booked.all())
    
    def remove_ticket(self, ticket):
        if ticket in self.tickets_booked.all():
            ticket.is_booked = False
            ticket.save()
            self.tickets_booked.remove(ticket)
            self.screening.increase_seat()
            self.screening.save()
            self.save()
    
    def delete(self, *args, **kwargs):
        for ticket in self.tickets_booked.all():
            ticket.is_booked = False
            ticket.screening.increase_seat()
            ticket.save()
        self.tickets_booked.clear()
        super().delete(*args, **kwargs)
        
    def __str__(self):
        return f"Booking for {self.user.username} at {self.screening.movie.title} on {self.screening.start_time}"

    