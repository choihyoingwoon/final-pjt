from django.shortcuts import render, redirect
from .models import Genre, Top_Movie, Now_Movie
from .serializers import TopMovieSerializer
from rest_framework.response import Response


# Create your views here.
def index(request):
    movies = Top_Movie.objects.all()
    serializer = TopMovieSerializer(movies, many=True)
    return Response(serializer.data)