from django.contrib import admin
from django.urls import path, include
from posts.views import FaceRecognitionAPIView
from users.views import UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.api.urls')),
    path('firebase-config/', include('core.api.urls')),
    path('api/face-recognition/', FaceRecognitionAPIView.as_view(), name='face-recognition'),
    path('api/users/create/', UserViewSet.as_view({'post': 'create'}), name='create_post'),
]
