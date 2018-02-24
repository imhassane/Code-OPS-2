from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from ...models import Profil
from ...forms import RegisterForm


def register(request):

    if request.user.is_authenticated:
        return redirect(reverse('main:home'))

    form = RegisterForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']

        user = User.objects.create_user(username=username, email=email, password=password)

        if user:
            profile = Profil(user=user)
            profile.save()
            return redirect(reverse('main:home'))

    return render(request, 'main/forms/register.html', {'form': form})
