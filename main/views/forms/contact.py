from django.shortcuts import render
from django.core.mail import send_mail
from ...forms import ContactForm


def contact(request):

    form = ContactForm(request.POST or None)

    # Variables de la page.
    context = {}

    context['form'] = form

    if form.is_valid():

        title = form.cleaned_data['title']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # On envoie le message.
        send_mail(title, message, 'codeopspro@gmail.com', [email])

        context['success'] = True
    
    else:
        # On ajoute les erreurs dans le contexte.
        context['errors'] = "Vérifiez vos informations."
    

    return render(request, 'main/forms/contact.html', context)