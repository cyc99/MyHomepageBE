from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = None
    password = None
    first_name = None
    last_name = None
    is_staff = None
    last_login = None
    is_superuser = None
    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = []
    
    email = models.EmailField()
    nickname = models.CharField(max_length=100)
    social_type = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.nickname