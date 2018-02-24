from django.views.generic import DetailView
from ...models import Course


class CourseDetail(DetailView):

    model = Course
    context_object_name = 'course'
    template_name = 'main/details/course.html'

