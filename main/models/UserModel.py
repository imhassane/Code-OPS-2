from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    added_date = models.DateTimeField(default="2018-02-01 00:00:00")

    class Meta:
        abstract = True
        ordering = ['-added_date', ]
