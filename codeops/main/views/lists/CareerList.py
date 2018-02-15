from django.views.generic import ListView
from ...models import Career, UserCareer


class CareerList(ListView):

    model = Career
    context_object_name = 'Careers'
    template_name = 'main/lists/careers.html'
    queryset = Career.objects.filter(visible=True)

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super(CareerList, self).get_context_data(object_list=object_list, **kwargs)

        # On récupère la liste des carrières suivies par l'utilisateur.
        user_careers = list()
        careers = UserCareer.objects.filter(user=self.request.user)

        for c in careers:
            user_careers.append(c.career)
        context['user_careers'] = user_careers

        return context
