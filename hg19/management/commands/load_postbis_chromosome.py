from django.core.management.base import BaseCommand
from optparse import make_option
from django.db.models.loading import get_model
from django.db.transaction import set_autocommit, commit
import hg19_example.settings as settings
from hg19.models import ChromosomeSequence
import os


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option(
                '--path',
                help="The path to the file that will be uploaded"),
        make_option(
                '--chromosome',
                help="Chromosome number"),
    )

    def handle(self, *args, **options):
        file_path = options.get('path')
        chromosome = options.get('chromosome')
        db_settings = settings.DATABASES['default']
        
        cf = open(file_path, 'r')
        nf_path = file_path + '.dump'
        nf = open(nf_path, 'w')
        nf.write(chromosome + '\t')
        l = 'line'
        while l:
            l = cf.readline()
            if l:
                l = l.strip().upper()
                if l.startswith('>'):
                    continue
                nf.write(l)
        cf.close()
        nf.close()
        
        cmd = "psql {db_name} -c '\COPY {db_table} (name, sequence) FROM {nf_path}'".format(db_name=db_settings['NAME'], db_table=ChromosomeSequence._meta.db_table, nf_path=nf_path)
        os.system(cmd)
        os.remove(nf_path)
