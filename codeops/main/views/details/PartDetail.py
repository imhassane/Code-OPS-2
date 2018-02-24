from django.views.generic import DetailView
from ...models import Part


class PartDetail(DetailView):

    model = Part
    template_name = 'main/details/part.html'
    context_object_name = 'part'
