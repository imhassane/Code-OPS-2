from django.views.generic import ListView
from ...models import Path, Career, UserPath
from django.shortcuts import get_object_or_404 as _g


class PathList(ListView):

    model = Path
    context_object_name = 'paths'
    template_name = 'main/lists/paths.html'

    def get_queryset(self):
        return Path.objects.filter(career=_g(Career, pk=self.kwargs['career_pk'])).filter(visible=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PathList, self).get_context_data(object_list=object_list, **kwargs)

        # On récupère la liste des paths déjà suivis par l'utilisateur.
        user_path = list()
        paths = UserPath.objects.filter(user=self.request.user)

        for c in paths:
            user_path.append(c.path)
        context['user_paths'] = user_path
        context['career'] = _g(Career, pk=self.kwargs['career_pk'])

        return context
