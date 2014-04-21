# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sequence4'
        db.create_table(u'hg19_sequence4', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence4'])

        # Adding model 'Sequence5'
        db.create_table(u'hg19_sequence5', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence5'])

        # Adding model 'Sequence6'
        db.create_table(u'hg19_sequence6', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence6'])

        # Adding model 'Sequence7'
        db.create_table(u'hg19_sequence7', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence7'])

        # Adding model 'Sequence2'
        db.create_table(u'hg19_sequence2', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence2'])

        # Adding model 'Sequence3'
        db.create_table(u'hg19_sequence3', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence3'])

        # Adding model 'Sequence8'
        db.create_table(u'hg19_sequence8', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence8'])

        # Adding model 'Sequence9'
        db.create_table(u'hg19_sequence9', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence9'])

        # Adding model 'Sequence22'
        db.create_table(u'hg19_sequence22', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence22'])

        # Adding model 'Sequence21'
        db.create_table(u'hg19_sequence21', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence21'])

        # Adding model 'Sequence20'
        db.create_table(u'hg19_sequence20', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence20'])

        # Adding model 'SequenceX'
        db.create_table(u'hg19_sequencex', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['SequenceX'])

        # Adding model 'SequenceY'
        db.create_table(u'hg19_sequencey', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['SequenceY'])

        # Adding model 'Sequence18'
        db.create_table(u'hg19_sequence18', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence18'])

        # Adding model 'Sequence19'
        db.create_table(u'hg19_sequence19', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence19'])

        # Adding model 'Sequence16'
        db.create_table(u'hg19_sequence16', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence16'])

        # Adding model 'Sequence17'
        db.create_table(u'hg19_sequence17', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence17'])

        # Adding model 'Sequence14'
        db.create_table(u'hg19_sequence14', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence14'])

        # Adding model 'Sequence15'
        db.create_table(u'hg19_sequence15', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence15'])

        # Adding model 'Sequence12'
        db.create_table(u'hg19_sequence12', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence12'])

        # Adding model 'Sequence13'
        db.create_table(u'hg19_sequence13', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence13'])

        # Adding model 'Sequence10'
        db.create_table(u'hg19_sequence10', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence10'])

        # Adding model 'Sequence11'
        db.create_table(u'hg19_sequence11', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence11'])


    def backwards(self, orm):
        # Deleting model 'Sequence4'
        db.delete_table(u'hg19_sequence4')

        # Deleting model 'Sequence5'
        db.delete_table(u'hg19_sequence5')

        # Deleting model 'Sequence6'
        db.delete_table(u'hg19_sequence6')

        # Deleting model 'Sequence7'
        db.delete_table(u'hg19_sequence7')

        # Deleting model 'Sequence2'
        db.delete_table(u'hg19_sequence2')

        # Deleting model 'Sequence3'
        db.delete_table(u'hg19_sequence3')

        # Deleting model 'Sequence8'
        db.delete_table(u'hg19_sequence8')

        # Deleting model 'Sequence9'
        db.delete_table(u'hg19_sequence9')

        # Deleting model 'Sequence22'
        db.delete_table(u'hg19_sequence22')

        # Deleting model 'Sequence21'
        db.delete_table(u'hg19_sequence21')

        # Deleting model 'Sequence20'
        db.delete_table(u'hg19_sequence20')

        # Deleting model 'SequenceX'
        db.delete_table(u'hg19_sequencex')

        # Deleting model 'SequenceY'
        db.delete_table(u'hg19_sequencey')

        # Deleting model 'Sequence18'
        db.delete_table(u'hg19_sequence18')

        # Deleting model 'Sequence19'
        db.delete_table(u'hg19_sequence19')

        # Deleting model 'Sequence16'
        db.delete_table(u'hg19_sequence16')

        # Deleting model 'Sequence17'
        db.delete_table(u'hg19_sequence17')

        # Deleting model 'Sequence14'
        db.delete_table(u'hg19_sequence14')

        # Deleting model 'Sequence15'
        db.delete_table(u'hg19_sequence15')

        # Deleting model 'Sequence12'
        db.delete_table(u'hg19_sequence12')

        # Deleting model 'Sequence13'
        db.delete_table(u'hg19_sequence13')

        # Deleting model 'Sequence10'
        db.delete_table(u'hg19_sequence10')

        # Deleting model 'Sequence11'
        db.delete_table(u'hg19_sequence11')


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
