from django.db import models
from django.contrib.auth.models import User
from hadrian.utils.slugs import unique_slugify

class App(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(editable=False)
    date_started = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    date_due = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    project_manager = models.ForeignKey(User, blank=True, null=True)
    client = models.CharField(max_length=250, blank=True, null=True) #This might be a foreig key
    site_url = models.URLField(max_length=500, blank=True, null=True)
    enable_chats = models.BooleanField(default=False)
    enable_repo = models.BooleanField(default=False)
    enable_issues = models.BooleanField(default=False)
    developers = models.ManyToManyField(User, related_name="app_developers", blank=True, null=True)
    
    def __unicode__(self): # pragma: no cover
        return self.name
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        super(App, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('projects.views.app', (), {'app_slug': self.slug})
    
    @property        
    def open_issues(self):
        return "5"
    
    

        
    
    