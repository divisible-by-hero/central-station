'''
    Author: Derek Stegelman
    Package: Projects App

'''

from django.db import models
from django.contrib.auth.models import User
from hadrian.utils.slugs import unique_slugify
from projects.choices import *
from issues.models import *

class App(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    enable_issues = models.BooleanField(default=False)
    users = models.ManyToManyField(User)
    
    def __unicode__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(App, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('projects.views.app', (), {'app_slug': self.slug})
    
    @property        
    def open_defects(self):
        return Issues.objects.open().by_app(self.slug).count()
    
    

        
    
    