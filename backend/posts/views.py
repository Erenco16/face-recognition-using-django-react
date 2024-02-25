from django.shortcuts import render
import cv2
import numpy as np
import urllib.request
from rest_framework.response import Response
from rest_framework.views import APIView
from .api.serializers import FaceEncodingSerializer

class FaceRecognitionAPIView(APIView):
    def post(self, request):
        image_url = request.data.get('image_url')
        
        # Fetch image from URL using urllib
        with urllib.request.urlopen(image_url) as url_response:
            image_data = url_response.read()
        
        # Convert image data to numpy array
        nparr = np.frombuffer(image_data, np.uint8)
        
        # Decode numpy array to OpenCV image format
        image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)
        
        face_encodings = []
        
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            encoding = [list(np.array(face).flatten())]
            face_encodings.append(encoding)
        
        serializer = FaceEncodingSerializer({'face_encodings': face_encodings})
        return Response(serializer.data)
