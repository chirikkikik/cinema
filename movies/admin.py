from django.contrib import admin
from .models import Movie, Screening

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'genre', 'target_audience')
    search_fields = ('title', 'genre')

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'movie', 'date', 'available_seats', 'total_seats', 'cinema_hall')
    list_filter = ('date', 'cinema_hall')
    search_fields = ('movie__title', 'cinema_hall')
    
    def start_time(self, obj):
        return obj.start_time.strftime('%H:%M')
