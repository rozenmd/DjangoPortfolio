from django import forms


class UrlsForm(forms.Form):
    url = forms.CharField(max_length=300)
