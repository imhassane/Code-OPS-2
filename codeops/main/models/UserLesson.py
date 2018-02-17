from .Lesson import Lesson
from django.db import models
from django.contrib.auth.models import User


class UserLesson(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
