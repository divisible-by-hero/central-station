# -*- coding: utf-8 -*-
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

        # Adding model 'Client'
        db.create_table('core_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal('core', ['Client'])

    def backwards(self, orm):
        # Deleting model 'Settings'
        db.delete_table('core_settings')

        # Deleting model 'Client'
        db.delete_table('core_client')

    models = {
        'core.client': {
            'Meta': {'object_name': 'Client'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        },
        'core.settings': {
            'Meta': {'object_name': 'Settings'},
            'application_name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['core']