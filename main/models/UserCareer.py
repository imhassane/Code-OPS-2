from django.db import models
from .Career import Career
from .UserModel import UserModel


class UserCareer(UserModel):

    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.career.title)
