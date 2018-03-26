from django.views.generic import DetailView
from ...models import Career, Path


class CareerDetail(DetailView):

    model = Career
    context_object_name = 'career'
    template_name = 'main/details/career.html'

    def get_context_data(self, **kwargs):
        context = super(CareerDetail, self).get_context_data(**kwargs)

        paths = Path.objects.filter(career=self.get_object())

        context['paths'] = paths

        return context
