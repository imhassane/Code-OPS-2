from django.views.generic import DetailView
from ...models import Path, Course


class PathDetail(DetailView):

    model = Path
    context_object_name = 'path'
    template_name = 'main/details/path.html'

    def get_context_data(self, **kwargs):

        context = super(PathDetail, self).get_context_data(**kwargs)

        context['courses'] = Course.objects.filter(path=self.get_object())

        return context
