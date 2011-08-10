from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Board(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    
    def __unicode__(self):
        return self.name
    
    def save(self):
        self.slug = slugify(self.name)
        super(Board, self).save()
    
class Post(models.Model):
    subject = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    author = models.ForeignKey(User)
    board = models.ForeignKey(Board)
    content = models.TextField()
    created_date = models.DateField(auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.subject
    
    def save(self):
        self.slug = slugify(self.subject)
        super(Post, self).save()
        
class Reply(models.Model):
    subject = models.CharField(max_length=250)
    post = models.ForeignKey(Post)
    author = models.ForeignKey(User)
    content = models.TextField()
    created_date = models.DateField(auto_now=True, auto_now_add=True)