from django.db import models

class ActivityMixin(object):
    def by_app(self, app_slug):
        return self.filter(application__slug=app_slug)

class ActivityQuerySet(QuerySet, ActivityMixin):
    pass

class ActivityManager(models.Manager, ActivityMixin):
    def get_query_set(self):
        return ActivityQuerySet(self.model, using=self._db)
 