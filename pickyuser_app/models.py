from django.db import models
from django.contrib.auth.models import AbstractUser # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/


# Create your models here.
class CustomUserMod(AbstractUser):
    display_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    homepage = models.URLField(null=True, blank=True, max_length=150)
    REQUIRED_FIELDS = ['homepage', 'age']

    def __str__(self):
        return self.username
