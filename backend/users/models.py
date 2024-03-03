from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    title = models.CharField(max_length = 200)
    user_email = models.CharField(max_length = 200, default="dummy@gmail.com")
    image_field = models.ImageField(blank=True)
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self):
       return f'User: {self.title}'
    