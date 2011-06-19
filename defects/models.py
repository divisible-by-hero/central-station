from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Defect(models.Model):
    title = models.CharField()
    reporter = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.title