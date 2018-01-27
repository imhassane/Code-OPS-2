from django.views.generic import ListView
from ...models import Path


class PathList(ListView):

    model = Path
    context_object_name = 'paths'
    template_name = 'main/lists/paths.html'
    queryset = Path.objects.filter(visible=True)
