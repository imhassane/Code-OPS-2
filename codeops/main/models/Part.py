from django.db.models import ImageField, URLField, ForeignKey, CASCADE
from .BaseModel import BaseCourseModel
from django.shortcuts import reverse


class Part(BaseCourseModel):

    avatar = ImageField(upload_to='parts/')
    url = URLField(default='')
    course = ForeignKey('Course', related_name='parts', on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse('main:part', kwargs={'pk': self.pk, 'part_slug': self.slug})
