from django.db.models import ImageField, URLField, ForeignKey, CASCADE, TextField
from .BaseModel import BaseCourseModel
from django.shortcuts import reverse


class Part(BaseCourseModel):

    avatar = ImageField(upload_to='parts/')
    url = URLField(default='')
    course = ForeignKey('Course', related_name='parts', on_delete=CASCADE)
    content = TextField(default="Aucun contenu pour ce cours")

    def get_absolute_url(self):
        return reverse('main:part', kwargs={'slug': self.slug})
