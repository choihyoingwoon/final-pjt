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



@api_view(['POST'])
def likes(request, user_pk, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        me = get_object_or_404(get_uset_model(), pk=user.pk)
        if me.like_movies.filter(pk=movie_pk).exists():
            me.like_movies.remove(movie.pk)
            isPicked=False
        else : 
            me.like_movies.add(movie.pk)
            isPicked = True
        return Response(isPicked)


@api_view(['POST'])
def my_like_list(request, user_pk):
    me = get_object_or_404(get_uset_model(), pk=user.pk)
    movie_list = []
    for movie_pk in request.data:
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        movie_list.append(serializer.data)
        return Response(movie_list)


