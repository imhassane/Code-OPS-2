from django import forms


# Formulaire de contact.
class ContactForm(forms.Form):

    # Raison du contact.
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Objet de votre message'
    }))

    # Email de la personne.
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entrez votre adresse email'
    }))

    # Message de la personne.
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entrez votre message'
    }))

    def clean(self):
        pass