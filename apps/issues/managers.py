from django.db.models.query import QuerySet
from django.db.models import Manager

class IssueMixin(object):
    def open(self):
        return self.filter(status="open")
        
    def by_app(self, app_slug):
        return self.filter(application__slug=app_slug)
    
class IssueQuerySet(QuerySet, IssueMixin):
    pass

class IssueManager(Manager, IssueMixin):
    def get_query_set(self):
        return IssueQuerySet(self.model, using=self._db)
        
