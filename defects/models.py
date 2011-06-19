from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from defects.choices import *
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
        super(Category, self).save()

class Defect(models.Model):
    title = models.CharField(max_length=250)
    reporter = models.ForeignKey(User)
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES)
    category = models.ForeignKey(Category)
    
    def __unicode__(self):
        return self.title