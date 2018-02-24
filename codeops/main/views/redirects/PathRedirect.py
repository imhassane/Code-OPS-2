from django.shortcuts import redirect, reverse, get_object_or_404 as _g
from ...models import UserCareer, UserPath, Career, Path
from django.contrib.auth.decorators import login_required


@login_required
def path_redirect(request, path_pk, career_pk):

    user = request.user
    path = _g(Path, pk=path_pk)
    career = _g(Career, pk=career_pk)

    user_career = _g(UserCareer, career=career, user=user)

    user_path = UserPath(user=user, path=path, user_career=user_career)
    user_path.save()

    return redirect(reverse('main:courses', kwargs={'path_pk': path_pk}))
