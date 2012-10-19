__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

from django.db import models
from django.contrib.auth.models import User

from sprints.choices import STORY_STATUS_CHOICES
from sprints.managers import SprintManager
from accounts.models import Team
from projects.models import Project

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

    objects = SprintManager()

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return "Sprint from %s through %s" % (str(self.start_date), str(self.end_date))

    def total_points(self):
        points = 0
        for story in self.story_set.all():
            points = points + story.points
        return points

    def completed_points(self):
        points = 0
        for story in self.story_set.all():
            if story.status == 'done':
                points = points + story.points
        return points

    @models.permalink
    def get_absolute_url(self):
        return ('sprint_detail', (), { 'account': self.team.organization.slug, 'id': self.id })

    @models.permalink
    def get_story_add(self):
        return ('story_add', (), {'account': self.team.organization.slug})

    @models.permalink
    def get_task_add(self):
        return ('task_add', (), {'account': self.team.organization.slug})

class Story(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    
    points = models.IntegerField(blank=False, null=False)
    sprint = models.ForeignKey(Sprint, null=True, blank=True)
    project = models.ForeignKey(Project, null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('story_edit', (), {'account': self.project.account.slug, 'pk': self.id})

    class Meta:
        ordering = ['position']


class Task(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True)
    ticket = models.URLField(blank=True, null=True)
    assigned = models.ForeignKey(User, null=True)

    story = models.ForeignKey(Story, null=True)

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('task_edit', (), {'account': self.story.sprint.team.organization.slug, 'pk': self.id})

class Roadblock(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    story = models.ForeignKey(Story, null=True, blank=False)

    def __unicode__(self):
        return self.title
        
        
class OrderedStory(AuditBase):
    story = models.ForeignKey(Story, null=True, blank=False)
    position = models.IntegerField(blank=False)
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True)
    