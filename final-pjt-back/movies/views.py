from django.shortcuts import render, redirect
from .models import Top_Movie, Now_Movie
from .serializers import TopMovieSerializer, NowMovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def top_movies(request):
    top_movies = Top_Movie.objects.all()
    serializer = TopMovieSerializer(top_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def now_movies(request):
    now_movies = Now_Movie.objects.all()
    serializer = NowMovieSerializer(now_movies, many=True)
    return Response(serializer.data)