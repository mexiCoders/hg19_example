from django.db import models

class SequenceField(models.TextField):
    description = "DNA sequence"

    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        super(SequenceField, self).__init__(*args, **kwargs)
        
    def db_type(self, connection):
        return 'dna_sequence'

