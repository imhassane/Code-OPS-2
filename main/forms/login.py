from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entre votre nom d\'utilisateur'
    }))

    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entez votre mot de passe'
    }))
