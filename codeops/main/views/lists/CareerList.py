from django.views.generic import ListView
from ...models import Career, UserCareer


class CareerList(ListView):

    model = Career
    context_object_name = 'Careers'
    template_name = 'main/lists/careers.html'
    queryset = Career.objects.filter(visible=True)
