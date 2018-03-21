from .UserModel import UserModel
from .Path import Path
from .UserCareer import UserCareer
from django.db import models


class UserPath(UserModel):

    path = models.ForeignKey(Path, on_delete=models.CASCADE)

    user_career = models.ForeignKey(UserCareer, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.path.title)