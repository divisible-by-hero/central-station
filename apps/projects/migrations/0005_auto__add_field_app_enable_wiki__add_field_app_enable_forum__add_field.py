# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'App.enable_wiki'
        db.add_column('projects_app', 'enable_wiki', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'App.enable_forum'
        db.add_column('projects_app', 'enable_forum', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'App.enable_defects'
        db.add_column('projects_app', 'enable_defects', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'App.enable_wiki'
        db.delete_column('projects_app', 'enable_wiki')

        # Deleting field 'App.enable_forum'
        db.delete_column('projects_app', 'enable_forum')

        # Deleting field 'App.enable_defects'
        db.delete_column('projects_app', 'enable_defects')


    models = {
        'projects.app': {
            'Meta': {'object_name': 'App'},
            'enable_defects': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enable_forum': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'enable_wiki': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
