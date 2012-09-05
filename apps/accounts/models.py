__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    sub_domain = models.CharField(max_length=250, blank=False, null=True)
    company_name = models.CharField(max_length=250, blank=True, null=True)
    users = models.ManyToManyField(User, null=True, blank=True)

    # Main.
    is_active = models.BooleanField()
    is_deleted = models.BooleanField()


    def __unicode__(self):
        return self.sub_domain