import urllib.request
import cv2
import numpy as np
import dlib
from rest_framework.response import Response
from rest_framework.views import APIView
from .api.serializers import FaceEncodingSerializer
from firebase_admin import db

def get_facial_encodings(request):
    image_url = request.data.get('image_url')

    # Fetch image from URL using urllib
    with urllib.request.urlopen(image_url) as url_response:
        image_data = url_response.read()

    # Convert image data to numpy array
    nparr = np.frombuffer(image_data, np.uint8)

    # Decode numpy array to OpenCV image format
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert the image to gray scale to improve computational efficiency
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Initialize face detector
    face_detector = dlib.get_frontal_face_detector()

    # Detect faces in the gray image
    faces = face_detector(gray_image)

    # Initialize face encoder
    face_encoder = dlib.shape_predictor("/Users/godfather/Desktop/Software/connect_django_to_react/backend/posts/models/shape_predictor_68_face_landmarks.dat")

    face_encodings = []

    for face in faces:
        # Extract facial landmarks
        landmarks = face_encoder(gray_image, face)
        
        # Convert landmarks to numpy array
        landmarks_np = np.array([[p.x, p.y] for p in landmarks.parts()])
        
        # Encode face (you can use landmarks_np for encoding or any other method you prefer)
        encoding = np.array(landmarks_np.flatten())
        face_encodings.append(encoding)

        return face_encodings
    

def save_to_the_database(facial_encodings):
    # Get a database reference to our posts
    ref = db.reference('https://console.firebase.google.com/project/test-react-app-f5032/database/test-react-app-f5032-default-rtdb/data/~2F/tests')

    # Read the data at the posts reference (this is a blocking operation)
    print(ref.get())

class FaceRecognitionAPIView(APIView):
    def post(self, request):
        face_encodings = get_facial_encodings(request)
        # Serialize face encodings
        data = {"face_encodings": face_encodings}
        serializer = FaceEncodingSerializer(data=data)
        
        if serializer.is_valid():
            return Response(serializer.data)

        else:
            return Response(501)