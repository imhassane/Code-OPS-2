from django.db.models import ImageField, ForeignKey, CASCADE
from .BaseModel import BaseCourseModel
from django.shortcuts import reverse


class Course(BaseCourseModel):

    avatar = ImageField(upload_to='courses/')
    path = ForeignKey('Path', related_name='courses', on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse('course', kwargs={'pk': self.pk, 'slug': self.slug})
