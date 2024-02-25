from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 200)
    body = models.TextField()

    def __str__(self):
       return f'Post: {self.title}'
    
class FirebaseConfig(models.Model):
    apiKey = models.CharField(max_length = 200)
    authDomain = models.CharField(max_length = 200)
    databaseURL = models.CharField(max_length = 200)
    projectId = models.CharField(max_length = 200)
    storageBucket = models.CharField(max_length = 200)
    messagingSenderId = models.CharField(max_length = 200)
    appId = models.CharField(max_length = 200)

    def __str__(self):
       return f'FirebaseConfig: {self.authDomain}'