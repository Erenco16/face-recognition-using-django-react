from rest_framework.viewsets import ModelViewSet

from .models import FirebaseFaceEncodings
from .serializers import FaceEncodingSerializer
from rest_framework.response import Response
from rest_framework import status
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import auth
# Create your views here.

def initialize_app():
    # Use a secure service account JSON file
    cred = credentials.Certificate("/Users/godfather/Desktop/Software/connect_django_to_react/backend/firebase_config/serviceAccount.json")

    app = firebase_admin.initialize_app(cred, {'databaseURL': 'https://test-react-app-f5032-default-rtdb.firebaseio.com'})
    return app

def get_user_uids():
    try:
        ref = db.reference("/users")
        user_uids = []
        data = ref.get()
        for key in data:
            user_uids.append(data[key]['user_uid'])
        return user_uids
    except Exception as e:
        print(f"Error while getting database: {e}")

def write_face_encodings_to_db(auth, app, request, user_email, user_uid, face_encodings):
    key = request.COOKIES.get('userUid')


    ref_face = db.reference("/face_encodings")
    ref_face.push().set({
            "title": f"{user_email}",
            "face_encodings": f"{face_encodings}",
            "user_uid": f"{user_uid}"
        })

def write_to_db(request, user_email, user_uid, face_encodings):
    app = initialize_app()
    write_face_encodings_to_db(auth, app, request, user_email, user_uid, face_encodings)

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
         # Call write_to_db function with extracted data
        write_to_db(self.request, title, user_uid, face_encodings)



    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
