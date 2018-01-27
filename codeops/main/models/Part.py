from django.db.models import ImageField, ForeignKey, CASCADE
from .BaseModel import BaseCourseModel
from django.shortcuts import reverse


class Part(BaseCourseModel):

    avatar = ImageField(upload_to='parts/')
    course = ForeignKey('Course', related_name='parts', on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse('part', kwargs={'pk': self.pk, 'slug': self.slug})
