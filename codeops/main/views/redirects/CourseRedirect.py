from django.contrib.auth.decorators import login_required
from ...models import Course, UserCourse, UserPath, Path
from django.shortcuts import get_object_or_404 as _g, redirect, reverse


@login_required
def course_redirect(request, course_slug, path_pk):

    user = request.user
    path = _g(Path, pk=path_pk)
    user_path = _g(UserPath, path=path, user=request.user)
    course = _g(Course, slug=course_slug)

    if user and course:
        user_course = UserCourse(user=user, course=course, user_path=user_path)
        user_course.save()
        return redirect(reverse('main:parts', kwargs={'course_slug': course_slug}))

    return redirect(reverse('main:home'))
