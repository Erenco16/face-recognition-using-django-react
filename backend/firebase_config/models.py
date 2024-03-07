from django.db import models
from django.utils import timezone

# Create your models here.

class FirebaseFaceEncodings(models.Model):
    title = models.CharField(max_length = 200, default="dummy@gmail.com")
    user_uid = models.CharField(max_length = 200)
    face_encodings = models.JSONField()
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
       return f'Face encodings of: {self.title}'
    