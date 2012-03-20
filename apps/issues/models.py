from __future__ import division
from django.db import models
from issues.managers import IssueManager
from django.contrib.auth.models import User
from issues.choices import *
from projects.models import App
from datetime import date
# Create your models here.

class Milestone(models.Model):
    name = models.CharField(max_length=200)
    app = models.ForeignKey(App)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    
    def __unicode__(self):
        return self.name
        
    @property
    def complete(self):
        issues = Issue.objects.by_milestone(self.id).count()
        if issues == 0:
            return True
        else:
            return False
    
    @property    
    def progress(self):
        closed = Issue.objects.closed().by_app(self.app.slug).by_milestone(self.id).count()
        all = Issue.objects.by_app(self.app.slug).by_milestone(self.id).count()
        if all != 0:
            return closed/all * 100
        else:
            return 0
            
    @property
    def open_issues(self):
        return Issue.objects.open().by_app(self.app.slug).by_milestone(self.id).count()
    
    @property
    def closed_issues(self):
        return Issue.objects.closed().by_app(self.app.slug).by_milestone(self.id).count()
    
    @property
    def past_due(self):
        if date.today() > self.due_date:
            return True
        else:
            return False

class Issue(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    priority = models.CharField(max_length=20, choices=ISSUE_PRIORITIES)
    description = models.TextField()
    url = models.URLField(blank=True)
    file = models.FileField(upload_to="issues/issue", null=True, blank=True)
    creator = models.ForeignKey(User, null=True, blank=True)
    assigned_to = models.ForeignKey(User, related_name="assignee", null=True, blank=True)
    creation_date = models.DateField(auto_now=False, auto_now_add=True)
    last_modified_date = models.DateField(editable=False, blank=True, null=True, auto_now=True)
    application = models.ForeignKey(App)
    milestone = models.ForeignKey(Milestone, null=True, blank=True)
    
    objects = IssueManager()
    
    def __unicode__(self):
        return self.description
    
    @models.permalink
    def get_absolute_url(self):
        return ('issues.views.issue_detail', (), {'app_slug': self.application.slug, 'issue_id': self.id})
    
    def close(self, user):
        # Do something
        self.status = "closed"
        self.save()
    
    def move_to_in_progress(self):
        self.status = "in-progress"
        self.save()
    
    class Meta:
        ordering = ['-id']
        
        
class Comment(models.Model):
    issue = models.ForeignKey(Issue)
    author = models.ForeignKey(User)
    comment = models.TextField(null=True, blank=True)
    creation_date = models.DateField(auto_now_add=True)
    creation_date_time = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="issues/comments", null=True, blank=True)
    
    def __unicode__(self):
        return self.comment
    
    @property
    def is_issue_author(self):
        if self.issue.creator == self.author:
            return True
        else:
            return False
    
    
    
    