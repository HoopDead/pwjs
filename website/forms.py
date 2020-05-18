from django.forms import ModelForm
from django import forms


class api_request_query(forms.Form):
    def __init__(self, *args, **kwargs):
        super(api_request_query, self).__init__(*args, **kwargs)
        self.fields['query'].widget.attrs.update({'class': 'form-control', 'id': 'queryInput'})

    query = forms.CharField(max_length=25, required=True)


class next_page_form(forms.Form):
    page = forms.IntegerField(initial = 1, required=False)