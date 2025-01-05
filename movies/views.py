from django.shortcuts import render
from .models import Movie, Screening


def home_page(request):
    movies = Movie.objects.all()
    return render(request, 'home_page.html', {'movies': movies})

def screening_list(request):
    screenings = Screening.objects.all()
    return render(request, 'screening_list.html', {'screenings': screenings})

