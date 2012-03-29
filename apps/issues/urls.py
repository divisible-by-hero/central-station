from django.conf.urls import patterns, include, url
from issues.api import IssueResource
from tastypie.api import Api
from issues.views import *

v1_api = Api(api_name="v1")
v1_api.register(IssueResource())

urlpatterns = patterns('',
    
    url(r'^(?P<app_slug>[-\w]+)/open/$', issue_filter, {'filter_type': 'open'}, name="open_app_issues"),
    url(r'^(?P<app_slug>[-\w]+)/closed/$', issue_filter, {'filter_type': 'closed'}, name="closed_app_issues"),
    url(r'^(?P<app_slug>[-\w]+)/close/(?P<issue_id>[-\w]+)/$', close_issue, name="close_issue",),
    url(r'^(?P<app_slug>[-\w]+)/inprogress/(?P<issue_id>[-\w]+)/$', move_to_in_progress, name="move_issue_to_in_progress"),
    url(r'^(?P<app_slug>[-\w]+)/nofilter/$', issue_filter, {'filter_type': 'all'}, name="no_filter_app_issues"),
    url(r'^(?P<app_slug>[-\w]+)/filter/$', issue_filter, name="issue_filter"),
    url(r'^(?P<app_slug>[-\w]+)/milestones/$', milestone_list),
    url(r'^(?P<app_slug>[-\w]+)/view/(?P<issue_id>\d+)/$', issue_detail, name="issue_detail"),
    url(r'^(?P<app_slug>[-\w]+)/add/$', add_issue, name="add_issue"),
    url(r'^(?P<app_slug>[-\w]+)/milestone/add/$', add_milestone, name="add_milestone"),
    url(r'^handle_comment/$', handle_comment, name="handle_comment"),
    
    url(r'^api/', include(v1_api.urls)),
    
)
