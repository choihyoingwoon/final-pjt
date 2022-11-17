from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Community, CommunityComment
from .serializers import CommunitySerializer, CommunityCommentSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def community_create(request):
    if request.method == 'GET':
        communities = Community.objects.all()
        serializer = CommunitySerializer(communities, many=True)
        return Response(serializer.data)
    
    else :
        serializer = CommunitySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def comment_create(request, community_pk):
    community = Community.objects.get(pk=community_pk)
    if request.method == 'GET' :
        comments = community.comments.all()
        serializer = CommunityCommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    else :
        serializer = CommunityCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, community=community)
            return Response(serializer.data, status=status.HTTP_201_CREATED)