
# from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.email

