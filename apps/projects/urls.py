from django.conf.urls.defaults import patterns, include, url
from projects.views import *
from projects.feeds import *

urlpatterns = patterns('',
    url(r'^apps/$', app_list, name="app_list"),
    url(r'^versions/$', version_list, name="version_list"),
    url(r'^newapp/$' , add_application, name="add_application"),
    url(r'^version/add/$', add_version, name="add_version"),
    url(r'^app/(?P<app_slug>[-\w]+)/$', app, name="app"),
    url(r'^app/(?P<app_slug>[-\w]+)/settings/$', settings, name="app"),
    url(r'^feed/$', AppFeed()),
#    # This is the pattern for ids or other integers
#    url(r'^edit/(?P<bookmark_id>\d+)/$', edit_bookmark, name="edit_bookmark"),

    url(r'^api/', include('projects.api.urls')),
#    
)
