# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Roadblock.created_date'
        db.alter_column('sprints_roadblock', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Roadblock.deleted_date'
        db.alter_column('sprints_roadblock', 'deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Sprint.created_date'
        db.alter_column('sprints_sprint', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Sprint.deleted_date'
        db.alter_column('sprints_sprint', 'deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Story.created_date'
        db.alter_column('sprints_story', 'created_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, null=True))

        # Changing field 'Story.deleted_date'
        db.alter_column('sprints_story', 'deleted_date', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):

        # Changing field 'Roadblock.created_date'
        db.alter_column('sprints_roadblock', 'created_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Roadblock.deleted_date'
        db.alter_column('sprints_roadblock', 'deleted_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Sprint.created_date'
        db.alter_column('sprints_sprint', 'created_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Sprint.deleted_date'
        db.alter_column('sprints_sprint', 'deleted_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Story.created_date'
        db.alter_column('sprints_story', 'created_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Story.deleted_date'
        db.alter_column('sprints_story', 'deleted_date', self.gf('django.db.models.fields.DateField')(null=True))

    models = {
        'accounts.account': {
            'Meta': {'object_name': 'Account'},
            'company_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'})
        },
        'accounts.team': {
            'Meta': {'object_name': 'Team'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'organization': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Account']"})
        },
        'sprints.roadblock': {
            'Meta': {'object_name': 'Roadblock'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'story': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sprints.Story']", 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        },
        'sprints.sprint': {
            'Meta': {'object_name': 'Sprint'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['accounts.Team']"})
        },
        'sprints.story': {
            'Meta': {'object_name': 'Story'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'deleted_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'points': ('django.db.models.fields.IntegerField', [], {}),
            'sprint': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sprints.Sprint']", 'null': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'})
        }
    }

    complete_apps = ['sprints']