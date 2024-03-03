from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # overwriting the default email value
    def perform_create(self, serializer):
        # Get the email value from the request or set it to a default value
        user_email = self.request.data.get('email', 'default@example.com')
        # Set the email field in the serializer data
        serializer.validated_data['user_email'] = user_email
        # Perform the creation of the user
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)