from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import Community, Comment
from .serializers import CommunitySerializer, CommentSerializer
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
@api_view(['GET', 'POST'])
def community_create(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)
    
    else :
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@login_required
@api_view(['PUT', 'DELETE'])
def community_update_delete(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)

    if request.user.community.filter(pk=community_pk).exists():
        if request.method == 'PUT':
            serializer = CommunitySerializer(community, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        else : 
            community.delete()
            return Response('게시글이 삭제되었습니다')

    return Response('본인이 작성한 글만 수정 및 삭제할 수 있습니다.')
        

@login_required
@api_view(['GET', 'POST'])
def comment_create(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    if request.method == 'GET' :
        comments = community.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    else :
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, community=community)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@login_required
@api_view(['PUT', 'DELETE'])
def comment_update_delete(request, community_pk, comment_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.user.comments.filter(pk=comment_pk).exists():
        if request.method == 'PUT':
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

        else : 
            comment.delete()
            return Response('댓글이 삭제되었습니다')

    return Response('본인이 작성한 댓글만 수정 및 삭제할 수 있습니다.')
 