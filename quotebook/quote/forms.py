from django import forms

class QuoteForm(forms.Form):
    author = forms.CharField(max_length=20)
    context = forms.CharField(widget=forms.Textarea)
    quote = forms.CharField(widget=forms.Textarea)

