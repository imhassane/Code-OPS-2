from django.views.generic import DetailView
from ...models.Course import Course


class CareerDetail(DetailView):

    model = Course
    context_object_name = 'career'
    template_name = 'main/details/career.html'

