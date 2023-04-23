from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Visit(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    specAn = models.CharField(max_length=255)
    nameAnim = models.CharField(max_length=255)
    nameAnim = models.CharField(max_length=255)
    reason = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    textArea = models.CharField(max_length=255)

    def str(self):
        return self.name