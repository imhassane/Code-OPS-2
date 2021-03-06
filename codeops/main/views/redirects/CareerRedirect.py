from django.shortcuts import redirect, reverse, get_object_or_404 as _g
from ...models import UserCareer, Career
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def career_redirect(request, username, career_pk):

    user = _g(User, username=username)
    career = _g(Career, pk=career_pk)

    user_career = UserCareer(user=user, career=career)
    user_career.save()

    return redirect(reverse('main:paths', kwargs={'career_pk': career_pk}))
