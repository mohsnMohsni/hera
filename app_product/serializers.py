from rest_framework import serializers
from .models import Comment, Like
from app_account.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(source='user', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
