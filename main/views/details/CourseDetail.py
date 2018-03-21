from django.views.generic import DetailView
from ...models import Course, Part


class CourseDetail(DetailView):

    model = Course
    context_object_name = 'course'
    template_name = 'main/details/course.html'

    def get_context_data(self, **kwargs):

        context = super(CourseDetail, self).get_context_data(**kwargs)

        # On recupere la liste des parties disponibles.
        parts = Part.objects.filter(course=self.get_object())

        context['parts'] = parts

        return context
