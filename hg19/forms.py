from django import forms

class SearchForm(forms.Form):
    seq = forms.CharField(required=False, label='DNA sequence', min_length=8, max_length=100)
    chromosome = forms.ChoiceField(label='Chromosome', required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['chromosome'].choices = [('', 'Any')] +  [(i, i) for i in range(1, 23)] + [('X', 'X'), ('Y', 'Y'), ('M', 'M')]


class LocalAlignmentForm(forms.Form):
    seq = forms.CharField(required=False, label='DNA sequence', min_length=12, max_length=200)
    chromosome = forms.ChoiceField(label='Chromosome', required=False)
    search_method = forms.ChoiceField(label='Search method', required=True)

    def __init__(self, *args, **kwargs):
        super(LocalAlignmentForm, self).__init__(*args, **kwargs)
        self.fields['chromosome'].choices = [('', 'Any')] +  [(i, i) for i in range(1, 23)] + [('X', 'X'), ('Y', 'Y'), ('M', 'M')]
        self.fields['search_method'].choices = [('PostBIS', 'PostBIS'), ('Postgresql', 'Postgresql')]
