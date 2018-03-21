from django.shortcuts import render
from ...models import Course, Path, Career

def search(request):
    # On recupère la recherche de l'utilisateur.
    query = request.GET['search']

    context = {}

    if query:
        careers = Career.objects.filter(title__icontains=query)
        paths = Path.objects.filter(title__icontains=query)
        courses = Course.objects.filter(title__icontains=query)

        context['query'] = query

        if len(careers) > 0:
            context['career_found'] = True
            context['careers'] = careers

        if len(paths) > 0:
            context['path_found'] = True
            context['paths'] = paths

        if len(courses) > 0:
            context['course_found'] = True
            context['courses'] = courses

        context['results'] = True
    else:
        context['results'] = False

    return render(request, 'main/forms/search.html', context)
