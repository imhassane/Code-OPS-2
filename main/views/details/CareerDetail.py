from django.views.generic import DetailView
from ...models import Career, Path, UserPath


class CareerDetail(DetailView):

    model = Career
    context_object_name = 'career'
    template_name = 'main/details/career.html'

    def get_context_data(self, **kwargs):
        context = super(CareerDetail, self).get_context_data(**kwargs)

        paths = Path.objects.filter(career=self.get_object())

        # On récupère la liste des parcours suivis par l'utilisateur.
        user_paths = UserPath.objects.all()
        user_paths = [p.path for p in user_paths]

        # On enregistre la liste des parcours suivis par l'utilisateur.
        user_paths_list = []

        for path in paths:
            if path in user_paths:
                user_paths_list.append(path)

        context['paths'] = paths
        context['user_paths'] = user_paths_list

        return context
