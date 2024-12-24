from django import forms
from .models import Movie, Screening

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'duration', 'release_date', 'target_audience']

class ScreeningForm(forms.ModelForm):
    class Meta:
        model = Screening
        fields = ['start_time', 'movie', 'cinema_hall', 'date',  'available_seats']
        