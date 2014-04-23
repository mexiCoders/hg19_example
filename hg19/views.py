from django.shortcuts import render
from forms import SearchForm
from django.db import models
from django.db.models.loading import get_model
import django_tables2 as tables
import time
from haystack.query import SearchQuerySet
from search_indexes import SequenceMIndex


class SearchResultsTable(tables.Table):
    chromosome = tables.Column()
    id = tables.Column()
    seq = tables.Column()


def search(request):
    limit = 1000
    order = 'id'
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
                            chromosome_to_search.append((m, m.__name__.replace('Sequence', '')))
                initial_time = time.time()
                if 'complex_search' in request.GET:
                    for S, c in chromosome_to_search:
                        q = S.objects.search_between(S, seq)
                        for s in q:
                            seqs.append({'id': s[0], 'seq': s[1], 'chromosome': c})
                elif 'search_postgres' in request.GET:
                    for S, c in chromosome_to_search:
                        q = S.objects.filter(seq__contains=seq).order_by(order)[:limit]
                        for s in q:
                            seqs.append({'id': s.id, 'seq': s.seq, 'chromosome': c})
                elif 'search_elasticsearch' in request.GET:
                    for S, c in chromosome_to_search:
                        q = SearchQuerySet().all().filter(text__contains=seq).models(S)
                        for r in q:
                            s = S.objects.get(id=r.pk)
                            # haystack or elasticsearch gives similar matches, not exact
                            if seq in s.seq:
                                seqs.append({'id': s.id, 'seq': s.seq, 'chromosome': c})
                                if len(seqs) > limit:
                                    break

                final_time = time.time()
                context['search_time'] = final_time - initial_time
                table = SearchResultsTable(seqs)
                context['table'] = table
                context['seqs'] = seqs

    context['form'] = form

    return render(request, 'hg19/search.html', context)
