from django.views.generic import ListView
from ...models import Course, Path, UserCourse
from django.shortcuts import get_object_or_404 as _g


class CourseList(ListView):

    model = Course
    context_object_name = 'courses'
    template_name = 'main/lists/courses.html'

    def get_queryset(self):
        return Course.objects.filter(visible=True).filter(path=_g(Path, pk=self.kwargs['path_pk']))
