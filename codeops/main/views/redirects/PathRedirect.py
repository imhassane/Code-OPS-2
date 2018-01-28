from django.shortcuts import redirect, reverse, get_object_or_404 as _g
from ...models import UserPath, Path
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def path_redirect(request, username, path_pk):

    user = _g(User, username=username)
    path = _g(Path, pk=path_pk)

    user_path = UserPath(user=user, path=path)
    user_path.save()

    return redirect(reverse('main:paths'))
