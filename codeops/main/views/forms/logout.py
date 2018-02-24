from django.contrib.auth import logout as lg
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, redirect


@login_required
def logout(request):
    lg(request)
    return redirect(reverse('main:login'))
