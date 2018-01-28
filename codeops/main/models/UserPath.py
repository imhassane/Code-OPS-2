from django.db import models
from .Path import Path
from django.contrib.auth.models import User


class UserPath(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    path = models.OneToOneField(Path, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.path.title)