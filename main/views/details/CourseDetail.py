from django.views.generic import DetailView
from ...models import Course, Part


class CourseDetail(DetailView):

    model = Course
    context_object_name = 'course'
    template_name = 'main/details/course.html'

    def get_context_data(self, **kwargs):

        context = super(CourseDetail, self).get_context_data(**kwargs)

        context['parts'] = Part.object.filter(course=self.get_object())

        return context
