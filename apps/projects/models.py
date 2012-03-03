'''
    Author: Derek Stegelman
    Package: Projects App

'''

from django.db import models
from django.contrib.auth.models import User
from hadrian.utils.slugs import unique_slugify
from projects.choices import *


class App(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    git_repo_dir = models.CharField(max_length=500, null=True, blank=True)
    enable_wiki = models.BooleanField(default=False)
    enable_forum = models.BooleanField(default=False)
    enable_defects = models.BooleanField(default=False)
    users = models.ManyToManyField(User)
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        unique_slugify(self, self.name)
        super(App, self).save()

    @models.permalink
    def get_absolute_url(self):
        return ('projects.views.app', (), {'app_slug': self.slug})
        
    def open_defects(self):
        return "6"
    
    

        
    
    