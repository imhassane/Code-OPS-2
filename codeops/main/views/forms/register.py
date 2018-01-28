from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from ...models import Profil
from ...forms import RegisterForm


def register(request):

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        user = User.objects.create_user(username=username, email=email, password=password)

        profile = Profil(user=user)

        if profile:
            return redirect(reverse('main:home'))
    return render(request, 'main/register.html')
