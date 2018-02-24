from django.views.generic import ListView
from ...models import Course, Path, UserCourse
from django.shortcuts import get_object_or_404 as _g


class CourseList(ListView):

    model = Course
    context_object_name = 'courses'
    template_name = 'main/lists/courses.html'

    def get_queryset(self):
        return Course.objects.filter(path=_g(Path, pk=self.kwargs['path_pk']))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CourseList, self).get_context_data(object_list=object_list, **kwargs)

        # On récupère la liste des cours déjà suivis par l'utilisateur.
        user_courses = list()
        courses = UserCourse.objects.filter(user=self.request.user)

        for c in courses:
            user_courses.append(c.course)
        context['user_courses'] = user_courses

        return context
