from django.core.management.base import BaseCommand
from optparse import make_option
from django.db.models.loading import get_model
from django.db.transaction import set_autocommit, commit

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
                '--path',
                help="The path to the file that will be uploaded"),
        make_option(
                '--chromosome',
                help="Chromosome number"),
        make_option(
                '--db_register_length',
                help="Database register length"),
        make_option(
                '--convert_to_upper',
                help="Convert every nucleotid to upper case."),
    )

    def handle(self, *args, **options):
        file_path = options.get('path')
        chromosome = options.get('chromosome')
        Sequence = get_model('hg19', 'Sequence{}'.format(chromosome))
        reg_len = options.get('db_register_length')
        if reg_len:
            reg_len = int(reg_len)
        else:
            reg_len = 200
        convert_to_upper = False
        ctu = options.get('convert_to_upper')
        if ctu and ctu.lower().startswith('t'):
            convert_to_upper = True

        commit_len = int(10000 / reg_len)

        # remove old data
        Sequence.objects.all().delete()

        f = open(file_path, 'r')
        l = 'line'
        i = 0
        ln = 0
        seq = ''
        pos = 0
        set_autocommit(False)
        while l:
            ln += 1
            l = f.readline()
            if l:
                l = l.strip()
                if l.startswith('>'):
                    continue
                if convert_to_upper:
                    seq += l.upper()
                else:
                    seq += l
                while len(seq) >= reg_len:
                    s = Sequence(seq=seq[:reg_len], position=pos)
                    s.save()
                    pos += len(seq[:reg_len])
                    seq = seq[reg_len:]
                    i += 1
                    if i % commit_len == 0:
                        print l, ln
                        commit()
        if seq:
            s = Sequence(seq=seq, position=pos)
            s.save()
        commit()
        set_autocommit(True)
        f.close()
