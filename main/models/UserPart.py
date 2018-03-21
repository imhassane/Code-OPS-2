from django.db import models
from .Part import Part
from .UserCourse import UserCourse
from .UserModel import UserModel


class UserPart(UserModel):

    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    validate = models.BooleanField(default=False)

    user_course = models.ForeignKey(UserCourse, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return "%s - %s" % (self.user.username, self.course.title)
