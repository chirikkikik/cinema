import uuid
from django.db import models
from bookings.models import Booking

class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, default=None, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, unique=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ], default='pending')

    def save(self, *args, **kwargs):
        if not self.transaction_id:
            self.transaction_id = str(uuid.uuid4())
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment {self.transaction_id}"
    
    class Meta:
        db_table = "Payment"

