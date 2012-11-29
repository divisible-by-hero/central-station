import datetime

from django.db.models.query import QuerySet
from django.db.models import Manager

__author__ = 'Derek Stegelman'
__date__ = '10/17/12'

class SprintQuerySet(QuerySet):
    def current(self):
        return self.filter(start_date__lte=datetime.date.today(), end_date__gte=datetime.date.today())

class SprintManager(Manager):

    def get_query_set(self):
        return SprintQuerySet(self.model, using=self._db)

    def current(self):
        return self.get_query_set().current()



