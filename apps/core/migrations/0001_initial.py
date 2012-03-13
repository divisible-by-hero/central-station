# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Settings'
        db.create_table('core_settings', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('application_name', self.gf('django.db.models.fields.CharField')(max_length=250)),
        ))
        db.send_create_signal('core', ['Settings'])


    def backwards(self, orm):
        
        # Deleting model 'Settings'
        db.delete_table('core_settings')


    models = {
        'core.settings': {
            'Meta': {'object_name': 'Settings'},
            'application_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']
