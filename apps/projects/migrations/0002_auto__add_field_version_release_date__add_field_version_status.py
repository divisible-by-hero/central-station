# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Version.release_date'
        db.add_column('projects_version', 'release_date', self.gf('django.db.models.fields.DateField')(default='development'), keep_default=False)

        # Adding field 'Version.status'
        db.add_column('projects_version', 'status', self.gf('django.db.models.fields.CharField')(default='development', max_length=250), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Version.release_date'
        db.delete_column('projects_version', 'release_date')

        # Deleting field 'Version.status'
        db.delete_column('projects_version', 'status')


    models = {
        'projects.app': {
            'Meta': {'object_name': 'App'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'projects.version': {
            'Meta': {'object_name': 'Version'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['projects.App']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['projects']
