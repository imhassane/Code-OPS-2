from django import forms


class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput({
        'class': 'uk-input uk-form-width-large'
    }))

    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'uk-input uk-form-width-large',
        'placeholder': 'Entez votre mot de passe'
    }))
