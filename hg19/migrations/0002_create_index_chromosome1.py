# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        db.execute("CREATE EXTENSION pg_trgm;")
        db.execute("CREATE INDEX trgm_hg19_sequence1_idx ON hg19_sequence1 USING gin (seq gin_trgm_ops);")

    def backwards(self, orm):
        db.execute("DROP INDEX trgm_hg19_sequence1_idx;")

    models = {
        u'hg19.sequence1': {
            'Meta': {'object_name': 'Sequence1'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'seq': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['hg19']
    symmetrical = True
