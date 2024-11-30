
from django.db import models

class Movie(models.Model):
    age_groups = (
        (0, "0+"), 
        (12, "12+"),
        (16, "16+"),
        (18, "18+")
    )
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.TextField(max_length = 30, default = (""), blank = False)
    description = models.TextField(default='No description yet.', blank=True)
    duration = models.DurationField()
    target_audience = models.IntegerField(choices = age_groups, default = 0)
    image = models.ImageField(upload_to='movies_images/', null=True, blank=True)
        
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'Movies'
        
        
class Cinema(models.Model):
    name_of_cinema = models.CharField(max_length=20, blank=False)
    total_auditoriums = models.PositiveIntegerField(default = 1)
    city = models.CharField(max_length=20, default=None, blank=False)
    adress = models.CharField(max_length=30, default=None, blank=False)
    
    def __str__(self):
        return f"{self.name_of_cinema}"
    
    class Meta:
        db_table = 'Cinemas'
        
    
class Audit(models.Model):
    total_seats = models.PositiveIntegerField(default=1)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, blank = False, related_name='auditoriums')
    
    def __str__(self):
        return f"{self.cinema.name_of_cinema}"
    
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        db_table = 'Auditoriums'
    

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings')
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE, related_name='screenings')
    start_at = models.TimeField()
    date = models.DateField()
    seats_remaining = models.PositiveIntegerField()
    
    def __str__(self):
        return f"{self.id}"
    
    class Meta:
        db_table = 'Screenings'
        
        
class Seat(models.Model):
    row = models.CharField(max_length=2)
    number = models.CharField(max_length=2)
    auditorium = models.ForeignKey(Audit, default=None, on_delete=models.CASCADE, related_name='seats')
    is_taken = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.number}, {self.row}"
    
    class Meta:
        db_table = 'Seats'
    
        
        





    
    










