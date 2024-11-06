
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null=False)
    genre = models.TextField(max_length = 30, default = (""), blank = False)
    description = models.TextField(default='No description yet.', blank=True)
    duration = models.PositiveIntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    target_audience = models.CharField(default="0+", max_length = 3)
    
    class Meta:
        db_table = 'Movies'
        
        
class Cinema(models.Model):
    name_of_cinema = models.CharField(max_length=20,blank=False)
    total_auditoriums = models.IntegerField()
    
    class Meta:
        db_table = 'Cinemas'
        
    
class Audit(models.Model):
    audit_name = models.TextField(max_length=30)
    total_seats = models.PositiveIntegerField(default=0)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, default = "", blank = False, related_name='auditoriums')
    
    class Meta:
        db_table = 'Auditoriums'
    

class Screening(models.Model):
    movie = models.ForeignKey(Movie, null=False, on_delete=models.CASCADE, related_name='screenings')
    audit = models.ForeignKey(Audit, null=False, on_delete=models.CASCADE, related_name='screenings')
    start_at = models.TimeField(null=False )
    date = models.DateField(default = (""), null=False)
    seats_remaining = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'Screenings'
        
        
class Seat(models.Model):
    row = models.CharField(max_length=1)
    number = models.CharField(max_length=2, default=0)
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE, related_name='seats')
    is_taken = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'Seats'
        
        





    
    










