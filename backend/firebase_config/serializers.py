from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import FirebaseFaceEncodings

class FaceEncodingSerializer(ModelSerializer):
    class Meta:
        model = FirebaseFaceEncodings
        fields = ('title', 'user_uid', 'face_encodings')