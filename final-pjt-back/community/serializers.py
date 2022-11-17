from rest_framework import serializers
from .models import Community, CommunityComment


class CommunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'


class CommunityCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunityComment
        fields = '__all__'

        