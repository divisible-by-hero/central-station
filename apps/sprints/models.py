from django.db import models
from django.contrib.auth.models import User

from actstream import action

from sprints.choices import STORY_STATUS_CHOICES, STORY_POINT_CHOICES, STATUS_COLORS, color_choices
from sprints.managers import SprintManager, SprintStoryManager
from accounts.models import Team, Account
from projects.models import Project

__author__ = 'Derek Stegelman, Garrett Pennington'
__date__ = '9/5/12'

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

    def create(self, request):
        action.send(request.user, verb='created', action_object=self, target=self.team)

    def update(self, request):
        action.send(request.user, verb='updated', action_object=self, target=self.team)

    @property
    def total_points(self):
        points = 0
        for sprint_story in SprintStory.objects.filter(sprint=self):
            points = points + sprint_story.points
        return points

    @property
    def completed_points(self):
        points = 0
        for sprint_story in SprintStory.objects.filter(sprint=self):
            # Remember to check for "Terminal" status
            if sprint_story.status.slug == 'done':
                points = points + sprint_story.points
        return points

    def completed_by_status(self):
        total = self.total_points
        perc = []
        for status in self.team.organization.statuses():
            stories_of_a_certain_status = []
            #statuses.append(status.status)
            for sprint_story in SprintStory.objects.filter(sprint=self):
                if sprint_story.status.slug == status.slug:
                    stories_of_a_certain_status.append(sprint_story)
            
            s = {
                'status' : status.status,
                'style_class': status.style_class
            }
            status_points = 0
            for sprint_story in stories_of_a_certain_status:
                status_points += sprint_story.points
            if total > 0:
                s['percentage'] = float(status_points) / float(total) * 100
            else:
                s['percentage'] = 0
            perc.append(s)

        return perc

    def complete(self, moved=True, sprint=None):
        """ Ask user if they want incomplete stories move to the next
         sprint, or moved to the backlog.  If moved to the next sprint,
         force user to create a new sprint object, and then create
         SprintStory objects for that next sprint.  Go ahead
         and use the attributes of the story for now when creating
         the new records.  Points/Status, etc.
        """

        # Get all SprintStory objects for this sprint.
        for sprint_story in SprintStory.objects.by_sprint(self):
            # Check to see if this story
            # is in Terminal state.
            if sprint_story.story.terminal:
                # It must be.  Add to new sprint object
                # or, move to backlog.
                if moved:
                    if sprint:
                        # Checking to make sure you provided
                        # a sprint.
                        SprintStory.objects.create(sprint=sprint, story=sprint_story.story, status=sprint_story.status, points=sprint_story.points)
                    else:
                        raise ValueError("You must provide a valid sprint to move this object to.")
                else:
                    # Backlog this bitch.
                    # Just realized I have no idea how to do that.  Ugh..
                    sprint_story.story.move_to_backlog()
            # pass
        
    @models.permalink
    def get_absolute_url(self):
        return ('sprint_detail', (), { 'account': self.team.organization.slug, 'id': self.id })

    @models.permalink
    def get_story_add(self):
        return ('story_add', (), {'account': self.team.organization.slug})

    @models.permalink
    def get_task_add(self):
        return ('task_add', (), {'account': self.team.organization.slug})

    @models.permalink
    def get_sprint_edit(self):
        return ('sprint_edit', (), { 'account': self.team.organization.slug, 'id': self.id })

class StoryStatus(models.Model):
    account = models.ForeignKey(Account, null=True)
    status = models.CharField(max_length=250, blank=True, null=True)
    order = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    color = models.CharField(max_length=20, choices=color_choices())
    terminal = models.BooleanField()
    
    def __unicode__(self):
        return self.status

    @property
    def style_class(self):
        return STATUS_COLORS[self.color]['style_class']

    @property
    def hex_code(self):
        return STATUS_COLORS[self.color]['hex']

    class Meta:
        ordering = ['order']


class Story(AuditBase):
    # Valid properties at the top.
    title = models.CharField(max_length=250, blank=False, null=True, help_text="As a User I would like to...")
    project = models.ForeignKey(Project, null=True)
    position = models.IntegerField(blank=True, null=True)

    # No Longer used.
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True, editable=False)
    story_status = models.ForeignKey(StoryStatus, null=True, blank=True)
    points = models.IntegerField(choices=STORY_POINT_CHOICES, blank=False, null=False, verbose_name="Difficulty")
    sprint = models.ForeignKey(Sprint, null=True, blank=True)

    def __unicode__(self):
        return self.title

    def create(self, request):
        action.send(request.user, verb='created', action_object=self, target=self.project)

    def close(self, request):
        self.status = 'done'
        action.send(request.user, verb='closed', action_object=self, target=self.project)
        self.save()

    def update(self, request):
        action.send(request.user, verb='updated', action_object=self, target=self.project)

    def mark_roadblocked(self, request):
        self.status = 'road-blocked'
        action.send(request.user, verb='marked as Road Blocked', action_object=self, target=self.project)

    def add_to_sprint(self, sprint):
        """ Add a story to a sprint, creates the story/sprint object
        """

        SprintStory.objects.create(sprint=sprint, story=self, status=self.story_status, points=self.points)

    def remove_from_sprint(self, sprint):
        """ Remove a story from a sprint.  Deletes the object because
         we do not want a historical record of this being attached to this sprint.
        """

        sprint_story_object = SprintStory.objects.get(sprint=sprint, story=self)
        sprint_story_object.delete()

    def move_to_backlog(self):
        raise NotImplementedError("Not sure if I need this.  Been drinking..")

    @models.permalink
    def get_absolute_url(self):
        return ('story_edit', (), {'account': self.project.account.slug, 'pk': self.id})

    @property
    def roadblocked(self):
        for task in self.task_set.all():
            if task.status == 'road-blocked':
                return True
        return False

    class Meta:
        ordering = ['story_status']


class Task(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    # Status not used anymore.
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True)
    ticket = models.URLField(blank=True, null=True)
    assigned = models.ForeignKey(User, null=True)

    story = models.ForeignKey(Story, null=True)
    complete = models.BooleanField()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('task_edit', (), {'account': self.get_account().slug, 'pk': self.id})

    def create(self, request):
        action.send(request.user, verb='created', action_object=self, target=self.story)

    def update(self, request):
        action.send(request.user, verb='updated', action_object=self, target=self.story)

    def get_account(self):
        story = SprintStory.objects.filter(story=self.story)[0]
        for story in story:
            return story.sprint.account

class Roadblock(AuditBase):
    title = models.CharField(max_length=250, blank=False, null=True)
    story = models.ForeignKey(Story, null=True, blank=False)

    def __unicode__(self):
        return self.title
        
        
class OrderedStory(AuditBase):
    story = models.ForeignKey(Story, null=True, blank=False)
    position = models.IntegerField(blank=False)
    status = models.CharField(choices=STORY_STATUS_CHOICES, max_length=20, blank=True, null=True)


class SprintStory(AuditBase):
    story = models.ForeignKey(Story, null=True, blank=False)
    sprint = models.ForeignKey(Sprint, null=True, blank=False)
    status = models.ForeignKey(StoryStatus, null=True, blank=True)
    points = models.IntegerField(choices=STORY_POINT_CHOICES, blank=False, null=True, verbose_name="Difficulty")

    objects = SprintStoryManager()

    def __unicode__(self):
        return "Story sprint object for %s %s" % (self.story, self.sprint)
