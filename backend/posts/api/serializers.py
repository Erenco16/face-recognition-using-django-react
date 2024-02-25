from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body')

class FaceEncodingSerializer(serializers.Serializer):
    face_encodings = serializers.ListField(child=serializers.ListField())