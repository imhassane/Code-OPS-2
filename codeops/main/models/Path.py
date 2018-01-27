from django.db.models import ImageField, ForeignKey, CASCADE
from .BaseModel import BaseCourseModel
from django.shortcuts import reverse


class Path(BaseCourseModel):

    avatar = ImageField(upload_to='paths/')
    career = ForeignKey('Career', related_name='paths', on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse('path', kwargs={'pk': self.pk, 'slug': self.slug})
