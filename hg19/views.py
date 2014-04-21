from django.shortcuts import render
from forms import SearchForm
from django.db import models
from django.db.models.loading import get_model
#from models import *


def search(request):
    context = {}
    form = SearchForm()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            seq = form.cleaned_data['seq']
            chromosome = form.cleaned_data['chromosome']
            if seq:
                seqs = []
                if chromosome:
                    Sequence = get_model('hg19', 'Sequence{}'.format(chromosome))
                    chromosome_to_search = [(Sequence, chromosome)]
                else:
                    chromosome_to_search = []
                    for m in models.get_models():
                        if m.__name__.startswith('Sequence'):
                            print m
                            chromosome_to_search.append((m, m.__name__.replace('Sequence', '')))
                for S, c in chromosome_to_search:
                    for s in S.objects.filter(seq__contains=seq):
                        seqs.append({'id': s.id, 'seq': s.seq, 'chromosome': c})

                context['seqs'] = seqs

    context['form'] = form

    return render(request, 'hg19/search.html', context)
