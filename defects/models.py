from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from defects.choices import *
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()

class Status(models.Model):
    status = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    
    def __unicode__(self):
        return self.status
    
    def save(self):
        self.slug = slugify(self.status)
        super(Status, self).save()


class Defect(models.Model):
    title = models.CharField(max_length=250)
    reporter = models.ForeignKey(User)
    status = models.ForeignKey(Status)
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    category = models.ForeignKey(Category)
    due_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.title