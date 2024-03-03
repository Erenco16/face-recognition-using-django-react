from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('title', 'user_email')