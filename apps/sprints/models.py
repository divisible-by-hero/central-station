__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

from django.db import models

from sprints.choices import STORY_STATUS_CHOICES
from accounts.models import Team

class AuditBase(models.Model):
    deleted = models.BooleanField()
    deleted_date = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)

    class Meta:
        abstract = True

class Sprint(AuditBase):
    name = models.CharField(max_length=250, blank=True, null=True)
    start_date = models.DateField(blank=False, null=True)
    end_date = models.DateField(blank=False, null=True)
    team = models.ForeignKey(Team) # TODO this should be M2M

    locked = models.BooleanField()

    def __unicode__(self):
        return self.name

class Story(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    
    points = models.IntegerField(blank=False, null=False)
    sprint = models.ForeignKey(Sprint, null=True)

    def __unicode__(self):
        return self.title
        
    class Meta:
        ordering = ['position']

class Roadblock(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    story = models.ForeignKey(Story, null=True, blank=False)

    def __unicode__(self):
        return self.title
        
        
class OrderedStory(AuditBase):
    story = models.ForeignKey(Story, null=True, blank=False)
    position = models.IntegerField(blank=False)
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True)
    