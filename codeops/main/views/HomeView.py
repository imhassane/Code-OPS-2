from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = 'main/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        context['home'] = True

        return context
