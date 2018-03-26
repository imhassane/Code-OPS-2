from django.contrib.auth.decorators import login_required
from ...models import Course, UserCourse
from django.shortcuts import get_object_or_404 as _g, redirect, reverse


@login_required
def course_redirect(request, slug):

    course = _g(Course, slug=slug)

    user_course = UserCourse(user=request.user, course=course)
    user_course.save()

    return redirect(reverse('main:course', kwargs={'slug': slug}))
