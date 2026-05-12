from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
  email = models.EmailField(unique=True)
  currency = models.CharField(max_length=3, default='USD')

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  def __str__(self):
    return self.email