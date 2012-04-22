from django.db import models

class Settings(models.Model):
    application_name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.application_name
        
class Client(models.Model):
    name = models.CharField(max_length=250, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True, null=True)
    
    def __unicode__(self):
        return self.name