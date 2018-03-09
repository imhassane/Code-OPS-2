from django.contrib.auth import logout as lg
from django.shortcuts import reverse, redirect


def logout(request):
    if request.user.is_authenticated:
        lg(request)
    return redirect(reverse('main:login'))
