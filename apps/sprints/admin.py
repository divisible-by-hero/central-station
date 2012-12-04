__author__ = 'Derek Stegelman'
__date__ = '9/6/12'
from django.contrib import admin

from sprints.models import Story, Roadblock, Sprint, Task, StoryStatus, SprintStory

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'story_status', 'sprint')
    list_editable = ['story_status']

class StoryStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'account')

class SprintAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date')

admin.site.register(Story, StoryAdmin)
admin.site.register(StoryStatus, StoryStatusAdmin)
admin.site.register(Roadblock)
admin.site.register(Sprint, SprintAdmin)
admin.site.register(Task)
admin.site.register(SprintStory)