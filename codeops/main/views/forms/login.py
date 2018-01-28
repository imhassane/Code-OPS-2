from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login as log, authenticate
from ...forms import LoginForm


def login(request):

    form = LoginForm(request.POST or None)

    if form.is_valid():
        username, password = form.cleaned_data['username'], form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)

        if user:
            log(request)
            return redirect(reverse('main:home'))

    return render(request, 'main/forms/login_form.html')
