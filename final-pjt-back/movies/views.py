from django.shortcuts import get_object_or_404
from .models import Movie, Review
from rest_framework import status
from .serializers import MovieSerializer, ReviewSerializer
from rest_framework.response import Response
# from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication



# Create your views here.
@api_view(['GET'])
def top_movies(request):
    top_movies = Movie.objects.all().order_by('-popularity')
    serializer = MovieSerializer(top_movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def now_movies(request):
    now_movies = Movie.objects.all().order_by('-release_date')[:20]
    serializer = MovieSerializer(now_movies, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)

    if request.method == 'GET':
        reviews = movie.reviews.all().order_by('-created_at')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    else : 
        if request.user.is_authenticated :
            print(request.data.get('item'))
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user = request.user, movie=movie)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else :
            return Response('Error')

                
@api_view(['DELETE'])
def review_update_delete(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.user.is_authenticated:
        review.delete()
        return Response('댓글이 삭제되었습니다')
    else :
        return Response('본인이 작성한 글만 수정 및 삭제할 수 있습니다.')



@api_view(['POST'])
# @permission_classes([IsAuthenticated])
# @authentication_classes([JSONWebTokenAuthentication])
def likes(request, user_pk, movie_pk):
    print(request.user)
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        me = get_object_or_404(get_user_model(), pk=user_pk)
        if me.like_movies.filter(pk=movie.pk).exists():
            me.like_movies.remove(movie.pk)
            isPicked = False
        else : 
            me.like_movies.add(movie.pk)
            isPicked = True
        return Response(isPicked)
    else :
        return Response('로그인필요')


@api_view(['POST'])
def likelist(request, user_pk):
    if request.user.is_authenticated:
        me = get_object_or_404(get_user_model(), pk=user_pk)
        movie_list = []
        for mymovie_pk in request.data.get('mymovies'):
            movie = get_object_or_404(Movie, pk=mymovie_pk)
            serializer = MovieSerializer(movie)
            movie_list.append(serializer.data)
        return Response(movie_list)


