from django.contrib.auth.models import User
from django.db import models


class Profil(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='users/', blank=True, null=True)
    added_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
