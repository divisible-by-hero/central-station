from django.conf.urls.defaults import patterns, include, url
from projects.views import *

urlpatterns = patterns('',
    url(r'^apps/$', app_list, name="app_list"),
    url(r'^newapp/$' , add_application, name="add_application"),
    url(r'^(?P<app_slug>[-\w]+)/$', app, name="app"),
    url(r'^(?P<app_slug>[-\w]+)/users/$', users, name="users"),
    url(r'^(?P<app_slug>[-\w]+)/users_add/$', add_users, name="add_users"),
    url(r'^(?P<app_slug>[-\w]+)/settings/$', settings, name="app"),
    
)
