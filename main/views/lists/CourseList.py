from django.views.generic import ListView
from ...models import Course


class CourseList(ListView):

    model = Course
    context_object_name = 'courses'
    template_name = 'main/lists/courses.html'
