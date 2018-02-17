from django.db import models
from .BaseModel import BaseCourseModel


class Lesson(BaseCourseModel):
    url = models.URLField()
