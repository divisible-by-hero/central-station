from django.db import models



class Settings(models.Model):
    application_name = models.CharField(max_length=250)
    
    
    def __unicode__(self):
        return self.application_name