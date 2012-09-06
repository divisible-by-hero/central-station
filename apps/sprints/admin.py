__author__ = 'Derek Stegelman'
__date__ = '9/6/12'
from django.contrib import admin

from sprints.models import Story, Roadblock, Sprint

admin.site.register(Story)
admin.site.register(Roadblock)
admin.site.register(Sprint)
