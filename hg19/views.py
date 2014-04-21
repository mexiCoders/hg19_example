from django.shortcuts import render
from forms import SearchForm
from models import Sequence1


def search(request):
    context = {}
    form = SearchForm()
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            seq = form.cleaned_data['seq']
            if seq:
                if len(seq) < 5:
                    #error
                    pass
                else:
                    seqs = Sequence1.objects.filter(seq__contains=seq)
                    context['seqs'] = seqs

    context['form'] = form


    return render(request, 'hg19/search.html', context)
