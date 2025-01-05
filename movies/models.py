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
    genre = models.TextField(max_length = 100, default = (""), blank = False)
    description = models.TextField(default='No description yet.', blank=True)
    duration = models.DurationField()
    target_audience = models.IntegerField(choices = age_groups, default = 0)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)
        
    def __str__(self):
        return f"{self.title}"
    
    class Meta:
        db_table = 'Movies'
    

class Screening(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='screenings')
    start_time = models.TimeField()
    date = models.DateField()
    available_seats = models.PositiveIntegerField()
    total_seats= models.PositiveIntegerField(default=0)
    cinema_hall = models.CharField(max_length=255)
    
    def decrease_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            self.save()
        else:
            raise ValueError("No available seats")
    
    def increase_seat(self):
        if self.available_seats < self.total_seats:
            self.available_seats += 1
            self.save()
            
        
    def __str__(self):
        return f"{self.movie.title} - {self.date} - {self.start_time}"
    
    class Meta:
        db_table = 'Screenings'
        
    
        
        





    
    










