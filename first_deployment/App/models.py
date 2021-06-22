from django.db import models

from django.contrib.auth.models import User

class user_entry(models.Model):

    user=models.OneToOneField(User, on_delete=models.CASCADE)

    images=models.ImageField(upload_to='media', blank=True)
    sites=models.URLField(blank=True)

    def __str__(self):
        return self.user


# Create your models here.
