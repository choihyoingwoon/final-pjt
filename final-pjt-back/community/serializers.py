from rest_framework import serializers
from .models import Community, Comment
from accounts.serializers import UserSerializer


class CommunitySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Community
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    community=CommunitySerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

        