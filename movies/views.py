from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Screening
from .serializers import MovieSerializer, ScreeningSerializer
import django_filters


def home_page(request):
    movies = Movie.objects.all()
    return render(request, 'home_page.html', {'movies': movies})


class MovieFilter(viewsets.ModelViewSet):
    genre = django_filters.CharFilter(field_name='genre__name', lookup_expr='icontains', label='Genre')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains', label='Title')
    
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = MovieFilter
    search_fields = ['title']
    
    
class ScreeningViewSet(viewsets.ModelViewSet):
    queryset = Screening.objects.all()
    serializer_class = ScreeningSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    


    
