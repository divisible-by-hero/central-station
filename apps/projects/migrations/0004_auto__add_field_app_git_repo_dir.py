# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'App.git_repo_dir'
        db.add_column('projects_app', 'git_repo_dir', self.gf('django.db.models.fields.CharField')(default='', max_length=500), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'App.git_repo_dir'
        db.delete_column('projects_app', 'git_repo_dir')


    models = {
        'projects.app': {
            'Meta': {'object_name': 'App'},
            'git_repo_dir': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
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
