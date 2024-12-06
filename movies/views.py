from django.shortcuts import render, redirect
from .models import Movie, Screening
from .forms import MovieForm, ScreeningForm


def home_page(request):
    movies = Movie.objects.all()
    return render(request, 'home_page.html', {'movies': movies})


def create_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = MovieForm()

    return render(request, 'movies/create_movie.html', {'form': form})


def create_screening(request):
    if request.method == 'POST':
        form = ScreeningForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('screening_list')
    else:
        form = ScreeningForm()

    return render(request, 'movies/create_screening.html', {'form': form})


def screening_list(request):
    screenings = Screening.objects.all()
    return render(request, 'movies/screening_list.html', {'screenings': screenings})
