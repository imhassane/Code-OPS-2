from django.shortcuts import render, get_object_or_404 as _g
from django.contrib.auth.decorators import login_required
from ...models import UserPath, UserCourse, UserPart, UserCareer
from ...models import Profil


@login_required
def dashboard(request):

    context = {}
    profil = _g(Profil, user=request.user)
    courses = UserCourse.objects.filter(user=request.user)

    context['profil'] = profil
    context['courses'] = courses

    return render(request, 'main/details/dashboard.html', context)
