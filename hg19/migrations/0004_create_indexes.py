# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        for i in range(2, 23):
            sql = 'CREATE INDEX trgm_hg19_sequence{i}_idx ON hg19_sequence{i} USING gin (seq gin_trgm_ops);'.format(i=i)
            db.execute(sql)

        db.execute('CREATE INDEX trgm_hg19_sequenceX_idx ON hg19_sequenceX USING gin (seq gin_trgm_ops);')
        db.execute('CREATE INDEX trgm_hg19_sequenceY_idx ON hg19_sequenceY USING gin (seq gin_trgm_ops);')

    def backwards(self, orm):
        for i in range(2, 23):
            db.execute("DROP INDEX trgm_hg19_sequence{i}_idx;".format(i=i))

        db.execute("DROP INDEX trgm_hg19_sequenceX_idx;")
        db.execute("DROP INDEX trgm_hg19_sequenceY_idx;")
        

    models = {
        u'hg19.sequence1': {
            'Meta': {'object_name': 'Sequence1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence10': {
            'Meta': {'object_name': 'Sequence10'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence11': {
            'Meta': {'object_name': 'Sequence11'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence12': {
            'Meta': {'object_name': 'Sequence12'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence13': {
            'Meta': {'object_name': 'Sequence13'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence14': {
            'Meta': {'object_name': 'Sequence14'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence15': {
            'Meta': {'object_name': 'Sequence15'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence16': {
            'Meta': {'object_name': 'Sequence16'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence17': {
            'Meta': {'object_name': 'Sequence17'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence18': {
            'Meta': {'object_name': 'Sequence18'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence19': {
            'Meta': {'object_name': 'Sequence19'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence2': {
            'Meta': {'object_name': 'Sequence2'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence20': {
            'Meta': {'object_name': 'Sequence20'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence21': {
            'Meta': {'object_name': 'Sequence21'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence22': {
            'Meta': {'object_name': 'Sequence22'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence3': {
            'Meta': {'object_name': 'Sequence3'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence4': {
            'Meta': {'object_name': 'Sequence4'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence5': {
            'Meta': {'object_name': 'Sequence5'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence6': {
            'Meta': {'object_name': 'Sequence6'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence7': {
            'Meta': {'object_name': 'Sequence7'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence8': {
            'Meta': {'object_name': 'Sequence8'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequence9': {
            'Meta': {'object_name': 'Sequence9'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequencex': {
            'Meta': {'object_name': 'SequenceX'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'hg19.sequencey': {
            'Meta': {'object_name': 'SequenceY'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hg19']
    symmetrical = True
