from django.contrib import admin
from django.urls import path, include
from posts.views import FaceRecognitionAPIView
from users.views import UserViewSet
from firebase_config.views import FaceEncodingViewSet, FaceEncodingComparisonViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
    path('firebase-config/', include('core.api.urls')),
    path('api/face-recognition/', FaceRecognitionAPIView.as_view(), name='face-recognition'),
    path('api/users/create/', UserViewSet.as_view({'post': 'create'}), name='create_post'),
    path('api/users/face-encodings/', FaceEncodingViewSet.as_view({'post': 'create'}), name='save_face_encodings'),
    path('api/users/compare-face-encodings/', FaceEncodingComparisonViewSet.as_view(), name='compare_face_encodings'),
]
