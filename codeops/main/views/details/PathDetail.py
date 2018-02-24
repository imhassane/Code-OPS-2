from django.views.generic import DetailView
from ...models import Path


class PathDetail(DetailView):

    model = Path
    context_object_name = 'path'
    template_name = 'main/details/path.html'

