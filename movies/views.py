from django.shortcuts import render
from .models import Movie


def home_page(request):
    movies = Movie.objects.all()
    return render(request, 'home_page.html', {'movies': movies})

