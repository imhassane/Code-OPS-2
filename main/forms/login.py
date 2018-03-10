from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput({
        'class': 'uk-input uk-form-width-large',
        'placeholder': 'Entre votre nom d\'utilisateur'
    }))

    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'uk-input uk-width-1-1@s uk-width-1-3@m',
        'placeholder': 'Entez votre mot de passe'
    }))
