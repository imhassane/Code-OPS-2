from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import reverse, redirect


@login_required
def logout(request):
    logout(request)
    return redirect(reverse('main:login'))
