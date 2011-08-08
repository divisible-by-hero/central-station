from django.db import models
from django.contrib.auth.models import User
# Slugify is a handy method to have around for use.
from django.template.defaultfilters import slugify
from projects.choices import *
# Create your models here.


class App(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
        super(App, self).save()
    

class Version(models.Model):
    app = models.ForeignKey(App)
    number = models.CharField(max_length=250)
    release_date = models.DateField()
    status = models.CharField(max_length=250, choices=PROJECT_CHOICES)
    
    def __unicode__(self):
        return self.number