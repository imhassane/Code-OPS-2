from django.db import models
from .Course import Course
from django.contrib.auth.models import User


class UserCourse(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.course.title)
