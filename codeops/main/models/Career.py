from django.db.models import ImageField
from .BaseModel import BaseCourseModel
from django.shortcuts import reverse


class Career(BaseCourseModel):

    avatar = ImageField(upload_to='careers/')

    def get_absolute_url(self):
        return reverse('career', kwargs={'pk': self.pk, 'slug': self.slug})
