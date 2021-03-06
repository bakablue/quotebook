from django import forms

class QuoteForm(forms.Form):
    author  = forms.CharField(max_length=20)
    context = forms.CharField(widget=forms.Textarea, required=False)
    quote   = forms.CharField(widget=forms.Textarea)

class UserForm(forms.Form):
    pseudo            = forms.CharField(max_length=20)
    mail              = forms.EmailField()
    password          = forms.CharField(widget = forms.PasswordInput())
    pass_confirmation = forms.CharField(widget = forms.PasswordInput())

class LoginForm(forms.Form):
    pseudo   = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
