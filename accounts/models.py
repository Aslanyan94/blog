from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} at {self.updated_time}"