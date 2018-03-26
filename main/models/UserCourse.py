from django.db import models
from .Course import Course
from .UserModel import UserModel


class UserCourse(UserModel):

    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.course.title)
