from django import forms

class SearchForm(forms.Form):
    seq = forms.CharField(required=False, label='DNA sequence', min_length=5, max_length=100)
    chromosome = forms.ChoiceField(label='Chromosome', required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['chromosome'].choices = [('', 'Any')] +  [(i, i) for i in range(1, 23)] + [('X', 'X'), ('Y', 'Y'), ('M', 'M')]
