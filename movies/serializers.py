from rest_framework import serializers
from .models import Movie, Screening


class ScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = '__all__'
        
        
class MovieSerializer(serializers.ModelSerializer):
    screenings = ScreeningSerializer(many=True, read_only=True, source='screenings')
    release_date = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = Movie
        fields = '__all__'
    
        


