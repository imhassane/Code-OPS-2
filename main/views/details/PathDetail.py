from django.views.generic import DetailView
from ...models import Path, Course, UserCourse


class PathDetail(DetailView):

    model = Path
    context_object_name = 'path'
    template_name = 'main/details/path.html'

    def get_context_data(self, **kwargs):

        context = super(PathDetail, self).get_context_data(**kwargs)

        courses = Course.objects.filter(path=self.get_object())

        # On recupere les cours suivis par l'utilisateur.
        user_courses = UserCourse.objects.all()
        user_courses = [c.course for c in user_courses]
        user_courses_list = []

        for course in courses:
            if course in user_courses:
                user_courses_list.append(course)

        context['courses'] = courses
        context['user_courses'] = user_courses_list

        return context
