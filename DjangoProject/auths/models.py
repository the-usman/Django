from django.db import models
from django.utils import timezone

# Create your models here.



class Sinup(models.Model) :
    user_types = [
        ('ad', 'admin'),
        ('us', 'user')
    ]
    name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='auth/')
    password = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    user_type = models.CharField(max_length=2, choices=user_types)
    createdAt = models.DateTimeField(default=timezone.now)