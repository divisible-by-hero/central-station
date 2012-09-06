__author__ = 'Derek Stegelman'
__date__ = '9/6/12'

from django.db import models

class AuditBase(models.Model):
    deleted = models.BooleanField()
    deleted_date = models.DateField(null=True, blank=True)
    created_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True