from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email_notifications = models.BooleanField()


    def __unicode__(self):
        return self.user.first_name