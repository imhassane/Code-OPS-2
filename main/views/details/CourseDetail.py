from django.views.generic import DetailView
from ...models import Course, Part


class CourseDetail(DetailView):

    model = Course
    context_object_name = 'course'
    template_name = 'main/details/course.html'

    def get_context_data(self, **kwargs):

        context = super(CourseDetail, self).get_context_data(**kwargs)

        course = self.get_object()

        course.views += 1
        course.save(commit=True)

        # On recupere la liste des parties disponibles.
        parts = Part.objects.filter(course=course)

        context['parts_title'] = [part.title for part in parts]
        context['parts'] = parts

        return context
