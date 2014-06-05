# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Sequence4.position'
        db.add_column(u'hg19_sequence4', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence5.position'
        db.add_column(u'hg19_sequence5', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence6.position'
        db.add_column(u'hg19_sequence6', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence7.position'
        db.add_column(u'hg19_sequence7', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence1.position'
        db.add_column(u'hg19_sequence1', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence2.position'
        db.add_column(u'hg19_sequence2', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence3.position'
        db.add_column(u'hg19_sequence3', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence8.position'
        db.add_column(u'hg19_sequence8', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence9.position'
        db.add_column(u'hg19_sequence9', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence22.position'
        db.add_column(u'hg19_sequence22', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence21.position'
        db.add_column(u'hg19_sequence21', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence20.position'
        db.add_column(u'hg19_sequence20', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'SequenceM.position'
        db.add_column(u'hg19_sequencem', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'SequenceX.position'
        db.add_column(u'hg19_sequencex', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'SequenceY.position'
        db.add_column(u'hg19_sequencey', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence18.position'
        db.add_column(u'hg19_sequence18', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence19.position'
        db.add_column(u'hg19_sequence19', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence16.position'
        db.add_column(u'hg19_sequence16', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence17.position'
        db.add_column(u'hg19_sequence17', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence14.position'
        db.add_column(u'hg19_sequence14', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence15.position'
        db.add_column(u'hg19_sequence15', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence12.position'
        db.add_column(u'hg19_sequence12', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence13.position'
        db.add_column(u'hg19_sequence13', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence10.position'
        db.add_column(u'hg19_sequence10', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)

        # Adding field 'Sequence11.position'
        db.add_column(u'hg19_sequence11', 'position',
                      self.gf('django.db.models.fields.IntegerField')(null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Sequence4.position'
        db.delete_column(u'hg19_sequence4', 'position')

        # Deleting field 'Sequence5.position'
        db.delete_column(u'hg19_sequence5', 'position')

        # Deleting field 'Sequence6.position'
        db.delete_column(u'hg19_sequence6', 'position')

        # Deleting field 'Sequence7.position'
        db.delete_column(u'hg19_sequence7', 'position')

        # Deleting field 'Sequence1.position'
        db.delete_column(u'hg19_sequence1', 'position')

        # Deleting field 'Sequence2.position'
        db.delete_column(u'hg19_sequence2', 'position')

        # Deleting field 'Sequence3.position'
        db.delete_column(u'hg19_sequence3', 'position')

        # Deleting field 'Sequence8.position'
        db.delete_column(u'hg19_sequence8', 'position')

        # Deleting field 'Sequence9.position'
        db.delete_column(u'hg19_sequence9', 'position')

        # Deleting field 'Sequence22.position'
        db.delete_column(u'hg19_sequence22', 'position')

        # Deleting field 'Sequence21.position'
        db.delete_column(u'hg19_sequence21', 'position')

        # Deleting field 'Sequence20.position'
        db.delete_column(u'hg19_sequence20', 'position')

        # Deleting field 'SequenceM.position'
        db.delete_column(u'hg19_sequencem', 'position')

        # Deleting field 'SequenceX.position'
        db.delete_column(u'hg19_sequencex', 'position')

        # Deleting field 'SequenceY.position'
        db.delete_column(u'hg19_sequencey', 'position')

        # Deleting field 'Sequence18.position'
        db.delete_column(u'hg19_sequence18', 'position')

        # Deleting field 'Sequence19.position'
        db.delete_column(u'hg19_sequence19', 'position')

        # Deleting field 'Sequence16.position'
        db.delete_column(u'hg19_sequence16', 'position')

        # Deleting field 'Sequence17.position'
        db.delete_column(u'hg19_sequence17', 'position')

        # Deleting field 'Sequence14.position'
        db.delete_column(u'hg19_sequence14', 'position')

        # Deleting field 'Sequence15.position'
        db.delete_column(u'hg19_sequence15', 'position')

        # Deleting field 'Sequence12.position'
        db.delete_column(u'hg19_sequence12', 'position')

        # Deleting field 'Sequence13.position'
        db.delete_column(u'hg19_sequence13', 'position')

        # Deleting field 'Sequence10.position'
        db.delete_column(u'hg19_sequence10', 'position')

        # Deleting field 'Sequence11.position'
        db.delete_column(u'hg19_sequence11', 'position')


    models = {
        u'hg19.chromosomesequence': {
            'Meta': {'object_name': 'ChromosomeSequence'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'sequence': ('hg19.fields.SequenceField', [], {})
        },
        u'hg19.sequence1': {
            'Meta': {'object_name': 'Sequence1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence10': {
            'Meta': {'object_name': 'Sequence10'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence11': {
            'Meta': {'object_name': 'Sequence11'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence12': {
            'Meta': {'object_name': 'Sequence12'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence13': {
            'Meta': {'object_name': 'Sequence13'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence14': {
            'Meta': {'object_name': 'Sequence14'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence15': {
            'Meta': {'object_name': 'Sequence15'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence16': {
            'Meta': {'object_name': 'Sequence16'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence17': {
            'Meta': {'object_name': 'Sequence17'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence18': {
            'Meta': {'object_name': 'Sequence18'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence19': {
            'Meta': {'object_name': 'Sequence19'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence2': {
            'Meta': {'object_name': 'Sequence2'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence20': {
            'Meta': {'object_name': 'Sequence20'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence21': {
            'Meta': {'object_name': 'Sequence21'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence22': {
            'Meta': {'object_name': 'Sequence22'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence3': {
            'Meta': {'object_name': 'Sequence3'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence4': {
            'Meta': {'object_name': 'Sequence4'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence5': {
            'Meta': {'object_name': 'Sequence5'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence6': {
            'Meta': {'object_name': 'Sequence6'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence7': {
            'Meta': {'object_name': 'Sequence7'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence8': {
            'Meta': {'object_name': 'Sequence8'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequence9': {
            'Meta': {'object_name': 'Sequence9'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequencem': {
            'Meta': {'object_name': 'SequenceM'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequencex': {
            'Meta': {'object_name': 'SequenceX'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        },
        u'hg19.sequencey': {
            'Meta': {'object_name': 'SequenceY'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'seq': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['hg19']