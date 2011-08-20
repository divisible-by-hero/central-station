from django.db import models
from django.contrib.auth.models import User
from profile.choices import *

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email_notifications = models.BooleanField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)


    def __unicode__(self):
        return self.user.first_name