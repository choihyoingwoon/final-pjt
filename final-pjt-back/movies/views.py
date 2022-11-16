from django.shortcuts import render, redirect
from .models import Top_Movie
from .serializers import TopMovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def index(request):
    movies = Top_Movie.objects.all()
    serializer = TopMovieSerializer(movies, many=True)
    return Response(serializer.data)