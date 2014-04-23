# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Sequence4.seq'
        db.alter_column(u'hg19_sequence4', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence5.seq'
        db.alter_column(u'hg19_sequence5', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence6.seq'
        db.alter_column(u'hg19_sequence6', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence7.seq'
        db.alter_column(u'hg19_sequence7', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence1.seq'
        db.alter_column(u'hg19_sequence1', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence2.seq'
        db.alter_column(u'hg19_sequence2', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence3.seq'
        db.alter_column(u'hg19_sequence3', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence8.seq'
        db.alter_column(u'hg19_sequence8', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence9.seq'
        db.alter_column(u'hg19_sequence9', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence22.seq'
        db.alter_column(u'hg19_sequence22', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence21.seq'
        db.alter_column(u'hg19_sequence21', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence20.seq'
        db.alter_column(u'hg19_sequence20', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SequenceM.seq'
        db.alter_column(u'hg19_sequencem', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SequenceX.seq'
        db.alter_column(u'hg19_sequencex', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'SequenceY.seq'
        db.alter_column(u'hg19_sequencey', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence18.seq'
        db.alter_column(u'hg19_sequence18', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence19.seq'
        db.alter_column(u'hg19_sequence19', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence16.seq'
        db.alter_column(u'hg19_sequence16', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence17.seq'
        db.alter_column(u'hg19_sequence17', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence14.seq'
        db.alter_column(u'hg19_sequence14', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence15.seq'
        db.alter_column(u'hg19_sequence15', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence12.seq'
        db.alter_column(u'hg19_sequence12', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence13.seq'
        db.alter_column(u'hg19_sequence13', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence10.seq'
        db.alter_column(u'hg19_sequence10', 'seq', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Sequence11.seq'
        db.alter_column(u'hg19_sequence11', 'seq', self.gf('django.db.models.fields.TextField')())

    def backwards(self, orm):

        # Changing field 'Sequence4.seq'
        db.alter_column(u'hg19_sequence4', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence5.seq'
        db.alter_column(u'hg19_sequence5', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence6.seq'
        db.alter_column(u'hg19_sequence6', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence7.seq'
        db.alter_column(u'hg19_sequence7', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence1.seq'
        db.alter_column(u'hg19_sequence1', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence2.seq'
        db.alter_column(u'hg19_sequence2', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence3.seq'
        db.alter_column(u'hg19_sequence3', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence8.seq'
        db.alter_column(u'hg19_sequence8', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence9.seq'
        db.alter_column(u'hg19_sequence9', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence22.seq'
        db.alter_column(u'hg19_sequence22', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence21.seq'
        db.alter_column(u'hg19_sequence21', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence20.seq'
        db.alter_column(u'hg19_sequence20', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'SequenceM.seq'
        db.alter_column(u'hg19_sequencem', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'SequenceX.seq'
        db.alter_column(u'hg19_sequencex', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'SequenceY.seq'
        db.alter_column(u'hg19_sequencey', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence18.seq'
        db.alter_column(u'hg19_sequence18', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence19.seq'
        db.alter_column(u'hg19_sequence19', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence16.seq'
        db.alter_column(u'hg19_sequence16', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence17.seq'
        db.alter_column(u'hg19_sequence17', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence14.seq'
        db.alter_column(u'hg19_sequence14', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence15.seq'
        db.alter_column(u'hg19_sequence15', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence12.seq'
        db.alter_column(u'hg19_sequence12', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence13.seq'
        db.alter_column(u'hg19_sequence13', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence10.seq'
        db.alter_column(u'hg19_sequence10', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Changing field 'Sequence11.seq'
        db.alter_column(u'hg19_sequence11', 'seq', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'hg19.sequence1': {
            'Meta': {'object_name': 'Sequence1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence10': {
            'Meta': {'object_name': 'Sequence10'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence11': {
            'Meta': {'object_name': 'Sequence11'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence12': {
            'Meta': {'object_name': 'Sequence12'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence13': {
            'Meta': {'object_name': 'Sequence13'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence14': {
            'Meta': {'object_name': 'Sequence14'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence15': {
            'Meta': {'object_name': 'Sequence15'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence16': {
            'Meta': {'object_name': 'Sequence16'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence17': {
            'Meta': {'object_name': 'Sequence17'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence18': {
            'Meta': {'object_name': 'Sequence18'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence19': {
            'Meta': {'object_name': 'Sequence19'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence2': {
            'Meta': {'object_name': 'Sequence2'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence20': {
            'Meta': {'object_name': 'Sequence20'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence21': {
            'Meta': {'object_name': 'Sequence21'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence22': {
            'Meta': {'object_name': 'Sequence22'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence3': {
            'Meta': {'object_name': 'Sequence3'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence4': {
            'Meta': {'object_name': 'Sequence4'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence5': {
            'Meta': {'object_name': 'Sequence5'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence6': {
            'Meta': {'object_name': 'Sequence6'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence7': {
            'Meta': {'object_name': 'Sequence7'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence8': {
            'Meta': {'object_name': 'Sequence8'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence9': {
            'Meta': {'object_name': 'Sequence9'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequencem': {
            'Meta': {'object_name': 'SequenceM'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequencex': {
            'Meta': {'object_name': 'SequenceX'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequencey': {
            'Meta': {'object_name': 'SequenceY'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hg19']