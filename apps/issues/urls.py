from django.conf.urls.defaults import patterns, include, url
from issues.views import *
from issues.feeds import IssueFeed

urlpatterns = patterns('',
    #url(r'^$', defect_list, name="defect_list"),
    url(r'^$', all_issues, name="all_issues"),
    #url(r'^view/(?P<defect_id>\d+)/$', defect_detail, name="defect_detail"),
    url(r'^app/(?P<app_slug>[-\w]+)/open/$', open_app_issues, name="open_app_issues"),
    url(r'^app/(?P<app_slug>[-\w]+)/closed/$', closed_app_issues, name="closed_app_issues"),
    url(r'^app/(?P<app_slug>[-\w]+)/nofilter/$', no_filter_app_issues, name="no_filter_app_issues"),
    url(r'^app/(?P<app_slug>[-\w]+)/milestones/$', milestone_list),
    url(r'^app/(?P<app_slug>[-\w]+)/view/(?P<defect_id>\d+)/$', defect_detail, name="defect_detail"),
    url(r'^app/(?P<app_slug>[-\w]+)/add/$', add_defect, name="add_defect"),
    url(r'^app/(?P<app_slug>[-\w]+)/milestone/add/$', add_milestone, name="add_milestone"),
#    # Homepage url , always name your URLS
#    url(r'^$', homepage, name="homepage"),
#    # URl with add and nothing after
#    url(r'^add/$', add, name="add_bookmark"),
#    # Feed URL
    #url(r'^feed/$', DefectFeed()),
#    # This is the pattern for ids or other integers
#    url(r'^edit/(?P<bookmark_id>\d+)/$', edit_bookmark, name="edit_bookmark"),
#    # This is the pattern for a slug, or alpha chars.
#    url(r'^slug/(?P<brew_slug>[-\w]+)/$', delete_bookmark, name="delete_bookmark"),
#    # Redirect to API urls.
    #url(r'^api/', include('defects.api.urls')),
#    
)
