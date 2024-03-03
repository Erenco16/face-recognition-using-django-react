from rest_framework.viewsets import ModelViewSet
from ..models import Post
from .serializers import PostSerializer
from rest_framework.permissions import AllowAny

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer