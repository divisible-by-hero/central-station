__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

from django.conf.urls import patterns, url, include

from tastypie.api import Api

from sprints.api import SprintResource
#from sprints.ajax import change_task, update_status
from sprints.views import SprintListView, update_story_status, update_stories, SprintDetailView, \
    StoryEditForm, AddStory, AddTask, TaskEditForm, Backlog, AddSprint, SprintEditForm, SprintStoryDetailView

v1_api = Api(api_name="v1")
v1_api.register(SprintResource())

urlpatterns = patterns('',

    #url(r'^(?P<goal_slug>[-\w]+)'),

    url(r'^$', SprintListView.as_view(), name='sprint_list'),
    url(r'^backlog/$', Backlog.as_view(), name='backlog'),

    url(r'^sprint/add/$', AddSprint.as_view(), name='sprint_add'),
    url(r'^sprint/edit/(?P<id>\d+)/$', SprintEditForm.as_view(), name='sprint_edit'),
    url(r'^sprint/(?P<id>\d+)/$', SprintStoryDetailView.as_view(), name='sprint_detail'),

    url(r'^stories/add/$', AddStory.as_view(), name='story_add'),
    url(r'^stories/(?P<pk>\d+)/$', StoryEditForm.as_view(), name='story_edit'),

    url(r'^task/add/$', AddTask.as_view(), name='task_add'),
    url(r'^task/(?P<pk>\d+)/$', TaskEditForm.as_view(), name='task_edit'),

    # As a Class....
    url(r'^class/(?P<pk>\d+)/$', SprintDetailView.as_view()),
    
    url(r'^update/story-status/$', update_story_status, name='update_story_status'),
    url(r'^update/stories/$', update_stories, name='update_stories'),
    # API
    url(r'^api/', include(v1_api.urls)),

    #AJAX
    #/ajax/update/task/13/?value=true
    #/ajax/update/story/24/?value=437

)
