from django.db import models
from django.contrib.auth.models import User
# Slugify is a handy method to have around for use.
from django.template.defaultfilters import slugify
from defects.choices import *
from projects.models import App, Version
# Create your models here.


class Defect(models.Model):
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    type = models.CharField(max_length=20, choices=DEFECT_TYPES)
    priority = models.CharField(max_length=20, choices=DEFECT_PRIORITIES)
    description = models.TextField()
    url = models.URLField(blank=True)
    creator = models.ForeignKey(User, null=True, blank=True)
    creation_date = models.DateField(auto_now=True, auto_now_add=True)
    last_modified_date = models.DateField(editable=False, blank=True)
    application = models.ForeignKey(App)
    version = models.ForeignKey(Version)
    
    def __unicode__(self):
        return self.description
    
    @models.permalink
    def get_absolute_url(self):
        return ('defects.views.defect_detail', (), {'defect_id': self.id})