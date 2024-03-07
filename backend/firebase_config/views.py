from rest_framework.viewsets import ModelViewSet
from .models import FirebaseFaceEncodings
from .serializers import FaceEncodingSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class FaceEncodingViewSet(ModelViewSet):
    queryset = FirebaseFaceEncodings.objects.all()
    serializer_class = FaceEncodingSerializer

    # overwriting the default email value
    def perform_create(self, serializer):
        # Get the email value from the request or set it to a default value
        title = self.request.data.get('title', 'default@example.com')
        # Set the email field in the serializer data
        serializer.validated_data['title'] = title
        # Perform the creation of the user
        user_uid = self.request.data.get('user_uid', 'user_uid_not_found')
        serializer.validated_data['user_uid'] = user_uid
        face_encodings = self.request.data.get('face_encodings', 'face_encoding_not_found')
        serializer.validated_data['face_encodings'] = face_encodings

        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
