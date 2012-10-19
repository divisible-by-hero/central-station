# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.account'
        db.add_column('projects_project', 'account',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounts.Account'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.account'
        db.delete_column('projects_project', 'account_id')


    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'projects.project': {
            'Meta': {'object_name': 'Project'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        }
    }

    complete_apps = ['projects']