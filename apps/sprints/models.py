__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

from django.db import models

class Story(models.Model):
    title = models.CharField(max_length=250, blank=False, null=True)

    def __unicode__(self):
        return self.title



class Sprint(models.Model):
    start_date = models.DateField(blank=False, null=True)
    end_date = models.DateField(blank=False, null=True)


    def __unicode__(self):
        return None
