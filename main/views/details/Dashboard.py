from django.shortcuts import render, get_object_or_404 as _g
from django.contrib.auth.decorators import login_required
from ...models import UserPath, UserCourse, UserPart, UserCareer, Profil
from ...models import Profil


@login_required
def dashboard(request):

    context = {}
    profil = None

    try:
        profil = Profil.objects.get(user=request.user)

    except:
        profil = Profil(user=request.user)
        profil.save()

    else:

        courses = UserCourse.objects.filter(user=request.user)
        paths = UserPath.objects.filter(user=request.user)
        careers = UserCareer.objects.filter(user=request.user)

        context['profil'] = profil

        context['courses'] = courses
        context['nb_courses'] = len(courses)

        context['paths'] = paths
        context['nb_paths'] = len(paths)

        context['careers'] = careers
        context['nb_careers'] = len(careers)

    return render(request, 'main/details/dashboard.html', context)
