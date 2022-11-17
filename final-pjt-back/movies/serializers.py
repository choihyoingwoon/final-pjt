from rest_framework import serializers
from .models import Top_Movie, Now_Movie


class TopMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Top_Movie
        fields = '__all__'
     
class NowMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Now_Movie
        fields = '__all__'