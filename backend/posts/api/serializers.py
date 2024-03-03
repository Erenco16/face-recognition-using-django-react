from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('username', 'user_email', 'image_field')

class FaceEncodingSerializer(serializers.Serializer):
    face_encodings = serializers.ListField(child=serializers.ListField())

class AddPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'user_email', 'image_field')