from django.core.management.base import BaseCommand
from optparse import make_option
from django.db.models.loading import get_model
from django.db.transaction import set_autocommit, commit

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
                '--path',
                help="the path to the file that will be uploaded"),
        make_option(
                '--chromosome',
                help="Chromosome number"),
    )

    def handle(self, *args, **options):
        file_path = options.get('path')
        chromosome = options.get('chromosome')
        Sequence = get_model('hg19', 'Sequence{}'.format(chromosome))
        f = open(file_path, 'r')
        l = 'line'
        i = 0
        set_autocommit(False)
        while l:
            l = f.readline()
            i += 1
            if l:
                l = l.strip()
                if l.startswith('>'):
                    continue
                s = Sequence(seq=l)
                s.save()
                if i % 2000 == 0:
                    print l, i
                    commit()
        commit()
        set_autocommit(True)
        f.close()


