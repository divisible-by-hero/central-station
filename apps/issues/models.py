from django.db import models
from issues.managers import IssueManager
from django.contrib.auth.models import User
from hadrian.utils.slugs import unique_slugify
from issues.choices import *
from projects.models import App
# Create your models here.

class Milestone(models.Model):
    name = models.CharField(max_length=200)
    app = models.ForeignKey(App)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    
    def __unicode__(self):
        return self.name

class Issue(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    priority = models.CharField(max_length=20, choices=ISSUE_PRIORITIES)
    description = models.TextField()
    url = models.URLField(blank=True)
    creator = models.ForeignKey(User, null=True, blank=True)
    creation_date = models.DateField(auto_now=False, auto_now_add=True)
    last_modified_date = models.DateField(editable=False, blank=True, null=True, auto_now=True)
    application = models.ForeignKey(App)
    milestone = models.ForeignKey(Milestone, null=True, blank=True)
    
    objects = IssueManager()
    
    def __unicode__(self):
        return self.description
    
    @models.permalink
    def get_absolute_url(self):
        return ('issues.views.defect_detail', (), {'app_slug': self.application.slug, 'defect_id': self.id})
        
        

