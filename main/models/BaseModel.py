from django.db import models


class SuperModel(models.Model):
    """ This will be the superclass of all the models in the app. """

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=400)
    visible = models.BooleanField(default=True)

    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    
    added_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class BaseCourseModel(SuperModel):
    """ This class will be the super class of the models Career, Path, Course, Part. """

    description = models.TextField(default="No description available")

    class Meta:
        abstract = True
