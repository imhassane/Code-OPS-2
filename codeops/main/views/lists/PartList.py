from django.views.generic import ListView
from ...models import Part, Course
from django.shortcuts import get_object_or_404 as _g


class PartList(ListView):
    model = Part
    template_name = 'main/lists/parts.html'
    context_object_name = 'parts'

    def get_queryset(self):

        return Part.objects.filter(course=_g(Course, slug=self.kwargs['course_slug']))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PartList, self).get_context_data(object_list=object_list, **kwargs)

        course = _g(Course, slug=self.kwargs['course_slug'])
        context['course'] = course

        return context
