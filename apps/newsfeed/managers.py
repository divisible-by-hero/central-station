from django.db import models


class GoalMixin(object):
    def visible(self):
        return self.filter(hidden=False)
    
    def hidden(self):
        return self.filter(hidden=True)
    
    def available(self):
        return self.filter(status="available")
    
    def current_instance(self, instance):
        return self.filter(current_instance=instance)
    
    def by_slug(self, slug):
        return self.filter(slug=slug)

class GoalQuerySet(QuerySet, GoalMixin):
    pass

class GoalManager(models.Manager, GoalMixin):
    def get_query_set(self):
        return GoalQuerySet(self.model, using=self._db)
