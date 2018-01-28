from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput({
        'class': 'uk-input'
    }))

    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'uk-input',
        'placeholder': 'Entez votre mot de passe'
        }))
