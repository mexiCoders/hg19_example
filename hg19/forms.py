from django import forms

class SearchForm(forms.Form):
    seq = forms.CharField(required=False, label='DNA sequence', min_length=5)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
