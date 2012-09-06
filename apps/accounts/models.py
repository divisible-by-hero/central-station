__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django.db import models
from django.contrib.auth.models import User

from hadrian.utils.slugs import unique_slugify

class Account(models.Model):
    company_name = models.CharField(max_length=250, blank=True, null=True)
    slug = models.SlugField()
    users = models.ManyToManyField(User, null=True, blank=True)

    # Main.
    is_active = models.BooleanField()
    is_deleted = models.BooleanField()

    def __unicode__(self):
        return self.sub_domain

    def save(self, *args, **kwargs):
        unique_slugify(self, self.company_name)
        super(Account, self).save(*args, **kwargs)

