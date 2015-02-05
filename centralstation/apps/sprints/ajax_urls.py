__author__ = 'Garrett Penninton #boom #thisislame'
__date__ = '9/5/12'

from django.conf.urls import patterns, url, include

#from tastypie.api import Api


from sprints.ajax import update_status, change_task

#v1_api = Api(api_name="v1")
#v1_api.register(SprintResource())

urlpatterns = patterns('',

    #AJAX
    #url(r'^task/(?P<task_id>\d+)/(?P<change>[-\w]+)/$', change_task, name='ajax_change_task'),
    #url(r'^story/status/(?P<story_id>\d+)/(?P<status_id>[-\w]+)/$', update_status, name='ajax_update_story'),

)
