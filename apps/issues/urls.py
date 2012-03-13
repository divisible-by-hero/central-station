from django.conf.urls.defaults import patterns, include, url
from issues.views import *

urlpatterns = patterns('',
    
    url(r'^app/(?P<app_slug>[-\w]+)/open/$', issue_filter, {'filter_type': 'open'}, name="open_app_issues"),
    url(r'^app/(?P<app_slug>[-\w]+)/closed/$', issue_filter, {'filter_type': 'closed'}, name="closed_app_issues"),
    url(r'^app/(?P<app_slug>[-\w]+)/close/(?P<issue_id>[-\w]+)/$', close_issue, name="close_issue",),
    url(r'^app/(?P<app_slug>[-\w]+)/inprogress/(?P<issue_id>[-\w]+)/$', move_to_in_progress, name="move_issue_to_in_progress"),
    url(r'^app/(?P<app_slug>[-\w]+)/nofilter/$', issue_filter, {'filter_type': 'all'}, name="no_filter_app_issues"),
    url(r'^app/(?P<app_slug>[-\w]+)/filter/$', issue_filter, name="issue_filter"),
    url(r'^app/(?P<app_slug>[-\w]+)/milestones/$', milestone_list),
    url(r'^app/(?P<app_slug>[-\w]+)/view/(?P<defect_id>\d+)/$', defect_detail, name="defect_detail"),
    url(r'^app/(?P<app_slug>[-\w]+)/add/$', add_defect, name="add_defect"),
    url(r'^app/(?P<app_slug>[-\w]+)/milestone/add/$', add_milestone, name="add_milestone"),
    url(r'^app/handle_comment/$', handle_comment, name="handle_comment"),
    
)
