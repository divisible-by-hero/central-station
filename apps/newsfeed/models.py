from django.db import models
from django.contrib.auth.models import User
from projects.models import App
from defects.models import Defect
from django.db.models.query import QuerySet

class ActivityMixin(object):
    def by_app(self, app_slug):
        return self.fliter(application__slug=app_slug)

class ActivityQuerySet(QuerySet, ActivityMixin):
    pass

class ActivityManager(models.Manager, ActivityMixin):
    def get_query_set(self):
        return ActivityQuerySet(self.model, using=self._db)
 

class Activity(models.Model):
    user = models.ForeignKey(User)
    action = models.CharField(max_length=400)
    application = models.ForeignKey(App, blank=True, null=True)
    defect = models.ForeignKey(Defect, blank=True, null=True)
    date_action = models.DateTimeField(auto_now=True, auto_now_add=True)
    
    objects = ActivityManager()
    
    def __unicode__(self):
        return "%s %s" % (self.user.username, self.action)


    class Meta:
        ordering = ['-date_action']