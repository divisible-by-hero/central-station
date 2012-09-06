__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

from django.db import models

from sprints.choices import STORY_STATUS
from accounts.models import Team

class AuditBase(models.Model):
    deleted = models.BooleanField()
    deleted_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True

class Sprint(AuditBase):
    name = models.CharField(max_length=250, blank=True, null=True)
    start_date = models.DateField(blank=False, null=True)
    end_date = models.DateField(blank=False, null=True)
    team = models.ForeignKey(Team)

    locked = models.BooleanField()

    def __unicode__(self):
        return self.name

class Story(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    status = models.CharField(choices=STORY_STATUS, max_length=20, blank=True, null=True)
    points = models.IntegerField(blank=False, null=False)
    sprint = models.ForeignKey(Sprint, null=True)

    def __unicode__(self):
        return self.title

class Roadblock(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    story = models.ForeignKey(Story, null=True, blank=False)

    def __unicode__(self):
        return self.title