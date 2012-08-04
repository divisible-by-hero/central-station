from django.db.models.query import QuerySet
from django.db.models import Q
from django.db.models import Manager

class IssueQuerySet(QuerySet)
    def open(self):
        return self.filter(Q(status="in-progress") | Q(status="open"))

    def by_app(self, app_slug):
        return self.filter(application__slug=app_slug)
    
    def closed(self):
        return self.filter(status="closed")
        
    def by_milestone(self, milestone_id):
        return self.filter(milestone__pk=milestone_id)
    

        
class IssueManager(Manager):
    def get_query_set(self):
        return IssueQuerySet(self.model, using=self._db)