from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entrez votre nom d\'utilisateur'
    }))

    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entrez votre mot de passe'
    }))
