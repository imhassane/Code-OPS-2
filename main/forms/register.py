from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entrez votre nom d\'utilisateur'
    }))

    password = forms.CharField(widget=forms.PasswordInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entez votre mot de passe'
    }))

    repeat = forms.CharField(widget=forms.PasswordInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Repetez votre mot de passe'
    }))

    email = forms.CharField(widget=forms.EmailInput({
        'class': 'uk-input uk-width-large@m uk-width-small@s',
        'placeholder': 'Entrez votre adresse email'
    }))

    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data['password']
        rptpassw = cleaned_data['repeat']

        if password != rptpassw:
            raise forms.ValidationError("Les mots de passe doivent être les mêmes")

