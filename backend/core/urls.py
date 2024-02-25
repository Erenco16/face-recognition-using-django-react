from django.contrib import admin
from django.urls import path, include
from posts.views import FaceRecognitionAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
    path('firebase-config/', include('core.api.urls')),
    path('api/face-recognition/', FaceRecognitionAPIView.as_view(), name='face-recognition'),
]
