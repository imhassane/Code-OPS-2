from django.views.generic import ListView
from ...models import Path, Career
from django.shortcuts import get_object_or_404 as _g


class PathList(ListView):

    model = Path
    context_object_name = 'paths'
    template_name = 'main/lists/paths.html'

    def get_queryset(self):
        paths = Path.objects.filter(career=_g(Career, self.kwargs['career_pk'])).filter(visible=True)
        return paths
