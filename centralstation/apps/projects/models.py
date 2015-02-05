from django.db import models

__author__ = 'Derek Stegelman'
__date__ = '10/17/12'

from accounts.models import Account

class Project(models.Model):
    title = models.CharField(max_length=250, blank=False, null=True)
    account = models.ForeignKey(Account, null=True)

    def __unicode__(self):
        return self.title