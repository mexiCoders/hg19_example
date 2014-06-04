from django.shortcuts import render
from forms import SearchForm, LocalAlignmentForm
from django.db import models
from django.db.models.loading import get_model
import django_tables2 as tables
import time
from haystack.query import SearchQuerySet
from search_indexes import SequenceMIndex
from django.utils.safestring import mark_safe
from models import ChromosomeSequence
import utils


class SeqColumn(tables.Column):
    def render(self, value, record, **kwords):
        query = kwords['table'].query
        html_seq = value.replace(query, '<span class="mark_text">{query}</span>'.format(query=query))
        return mark_safe(html_seq)

class SearchResultsTable(tables.Table):
    def __init__(self,  *args, **kwargs):
        self.query = kwargs.pop('query')
        super(SearchResultsTable, self).__init__(*args, **kwargs)

    class Meta:
        attrs = {"class": "table table-striped table-bordered table-condensed"}

    chromosome = tables.Column()
    id = tables.Column()
    seq = SeqColumn(verbose_name='Sequence')


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
                elif 'search_postbis' in request.GET:
                    if chromosome:
                        cs = ChromosomeSequence.objects.filter(name=chromosome)
                    else:
                        cs = ChromosomeSequence.objects.all()
                    for c in cs:
                        pos = ChromosomeSequence.objects.find_all_positions(c, seq)
                        for p in pos:
                            seqs.append({'id': p, 'seq': c.get_substring(p-20, 40+len(seq)), 'chromosome': c.name})

                final_time = time.time()
                context['search_time'] = final_time - initial_time
                table = SearchResultsTable(seqs, query=seq)
                context['table'] = table
                context['seqs'] = seqs

    context['form'] = form
    return render(request, 'hg19/search.html', context)


class SequencesColumn(tables.Column):
    def render(self, value, record, **kwords):
        split = value.split(',')
        html_seq = '{}<br>{}'.format(split[0], split[1])
        return mark_safe(html_seq)

class LocalAlignmentTable(tables.Table):
    class Meta:
        attrs = {"class": "table table-striped table-bordered table-condensed"}

    chromosome = tables.Column()
    position = tables.Column()
    score = tables.Column()
    sequences = SequencesColumn(verbose_name='Sequences')

def local_alignment(request):
    context = {}
    form = LocalAlignmentForm()
    if request.method == 'GET' and 'search' in request.GET:
        form = LocalAlignmentForm(request.GET)
        if form.is_valid():
            seq = form.cleaned_data['seq']
            chromosome = form.cleaned_data['chromosome']
            if seq:
                if chromosome:
                    Sequence = get_model('hg19', 'Sequence{}'.format(chromosome))
                    chromosome_to_search = [(Sequence, chromosome)]
                else:
                    chromosome_to_search = []
                    for m in models.get_models():
                        if m.__name__.startswith('Sequence'):
                            chromosome_to_search.append((m, m.__name__.replace('Sequence', '')))
                initial_time = time.time()
                method = form.cleaned_data['search_method']
                if method == 'PostBIS':
                    if chromosome:
                        cs = ChromosomeSequence.objects.filter(name=chromosome)
                    else:
                        cs = ChromosomeSequence.objects.all()
                    rows = []
                    for c in cs:
                        length = 10000
                        start = 0
                        c_length = c.get_length()
                        while start < c_length:
                            c_seq = c.get_substring(start, length)
                            alns = utils.local_alignment(c_seq, seq)
                            if alns:
                                aln_c, aln_seq, score, begin, end = alns[0]
                                b = begin
                                if b > 20:
                                    b = b - 20
                                e = end + 20
                                row = {'chromosome': c.name, 'position': start+begin, 'score': score, 'sequences': aln_c[b:e] + ',' + aln_seq[b:e]}
                                rows.append(row)
                            start += length
                    table = LocalAlignmentTable(rows)
                    context['table'] = table

                final_time = time.time()
                context['search_time'] = final_time - initial_time
    context['form'] = form
    return render(request, 'hg19/local_alignment.html', context)
