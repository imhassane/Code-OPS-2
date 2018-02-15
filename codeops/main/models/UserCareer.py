from django.db import models
from .Career import Career
from django.contrib.auth.models import User


class UserCareer(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    career = models.OneToOneField(Career, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.career.title)
