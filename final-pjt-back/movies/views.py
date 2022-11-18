from django.shortcuts import get_object_or_404
from .models import Movie, Review
from rest_framework import status
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required


# Create your views here.
@api_view(['GET'])
def top_movies(request):
    top_movies = Movie.objects.all().order_by('-popularity')
    serializer = MovieSerializer(top_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def now_movies(request):
    now_movies = Movie.objects.all().order_by('-release_date')[:10]
    serializer = MovieSerializer(now_movies, many=True)
    return Response(serializer.data)


@login_required
@api_view(['GET', 'POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        reviews = movie.comment_set.all
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    else : 
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

                
@login_required
@api_view(['PUT', 'DELETE'])
def review_update_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.user == review.user:
        if request.method == 'PUT':
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            
        else :
            review.delete()
            return Response('댓글이 삭제되었습니다')
    return Response('본인이 작성한 글만 수정 및 삭제할 수 있습니다.')


@login_required
@api_view(['POST'])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    context = {
        'like_count' : movie.like_users.count()
    }
    return Response(context)