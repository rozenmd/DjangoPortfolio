from django import forms
from web.models import UrlRequest


class UrlsForm(forms.Form):
    url = forms.CharField(max_length=300)

    class Meta:
            model = UrlRequest
            fields = ('url')
