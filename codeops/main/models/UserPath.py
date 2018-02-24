from django.db import models
from .Path import Path
from .UserCareer import UserCareer
from django.contrib.auth.models import User


class UserPath(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)

    user_career = models.ForeignKey(UserCareer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.path.title)