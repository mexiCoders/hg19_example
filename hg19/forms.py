from django import forms
from crispy_forms.helper import FormHelper
from models import ChromosomeSequence

class SearchForm(forms.Form):
    seq = forms.CharField(required=False, label='DNA sequence', min_length=8, max_length=100)
    chromosome = forms.ChoiceField(label='Chromosome', required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['chromosome'].choices = [('', 'Any')] +  [(i, i) for i in range(1, 23)] + [('X', 'X'), ('Y', 'Y'), ('M', 'M')]
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'

class LocalAlignmentForm(forms.Form):
    seq = forms.CharField(required=False, label='DNA sequence', min_length=12, max_length=200)
    chromosome = forms.ChoiceField(label='Chromosome', required=False)
    search_method = forms.ChoiceField(label='Search method', required=True)

    def __init__(self, *args, **kwargs):
        super(LocalAlignmentForm, self).__init__(*args, **kwargs)

        chromosomes = [('', 'Any')]
        for c in ChromosomeSequence.objects.all():
            chromosomes.append((c.id, c.name))

        self.fields['chromosome'].choices = chromosomes
        self.fields['search_method'].choices = [('pairwise2', 'pairwise2'), ('swalign', 'swalign')]
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_class = 'form-inline'

