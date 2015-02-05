__author__ = 'Derek Stegelman'
__date__ = '10/17/12'

from django.contrib import admin

from projects.models import Project


admin.site.register(Project)