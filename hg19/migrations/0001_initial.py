# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Sequence1'
        db.create_table(u'hg19_sequence1', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('seq', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'hg19', ['Sequence1'])


    def backwards(self, orm):
        # Deleting model 'Sequence1'
        db.delete_table(u'hg19_sequence1')


    models = {
        u'hg19.sequence1': {
            'Meta': {'object_name': 'Sequence1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hg19']