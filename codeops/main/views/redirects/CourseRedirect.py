from django.contrib.auth.decorators import login_required
from ...models import Course, UserCourse
from django.shortcuts import get_object_or_404 as _g, redirect, reverse
from django.contrib.auth.models import User


@login_required
def course_redirect(request, username, course_slug):

    user = _g(User, username=username)
    course = _g(Course, slug=course_slug)

    if user and course:
        user_course = UserCourse(user=user, course=course)
        user_course.save()
        return redirect(reverse('main:parts', kwargs={'course_slug': course_slug}))

    return redirect(reverse('main:home'))
