from django.shortcuts import render, reverse, redirect


def home(request):

    # Si l'utilisateur est connecté, on le redirige vers le tableau de bord.
    if request.user.is_authenticated:
        return redirect(reverse('main:dashboard'))

    return render(request, 'main/home.html', {home: True})
