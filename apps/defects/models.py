from django.db import models
from django.db.models.query import QuerySet
from django.contrib.auth.models import User
from nutsbolts.utils.slugs import unique_slugify
from defects.choices import *
from projects.models import App, Version
# Create your models here.

class DefectMixin(object):
    def open(self):
        return self.filter(status="open")
        
    def by_app(self, app_slug):
        return self.filter(application__slug=app_slug)
    
class DefectQuerySet(QuerySet, DefectMixin):
    pass

class DefectManager(models.Manager, DefectMixin):
    def get_query_set(self):
        return DefectQuerySet(self.model, using=self._db)
        

class Defect(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    type = models.CharField(max_length=20, choices=DEFECT_TYPES)
    priority = models.CharField(max_length=20, choices=DEFECT_PRIORITIES)
    description = models.TextField()
    url = models.URLField(blank=True)
    creator = models.ForeignKey(User, null=True, blank=True)
    creation_date = models.DateField(auto_now=True, auto_now_add=True)
    last_modified_date = models.DateField(editable=False, blank=True)
    application = models.ForeignKey(App)
    version = models.ForeignKey(Version)
    
    objects = DefectManager()
    
    def __unicode__(self):
        return self.description
    
    
    
    @models.permalink
    def get_absolute_url(self):
        return ('defects.views.defect_detail', (), {'app_slug': self.application.slug, 'defect_id': self.id})
        
        