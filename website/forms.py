from django.forms import ModelForm
from django import forms


class api_request_query(forms.Form):
    query = forms.CharField(max_length=25, required=True)