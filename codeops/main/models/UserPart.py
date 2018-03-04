from django.db import models
from .Part import Part
from .UserCourse import UserCourse
from django.contrib.auth.models import User


class UserPart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    validate = models.BooleanField(default=False)

    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.course.title)
