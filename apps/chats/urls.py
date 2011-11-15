from django.conf.urls.defaults import patterns, include, url
from chats.views import *

urlpatterns = patterns('',
    url(r'^$', rooms),
    url(r'^room/(?P<room_slug>[-\w]+)/$', room, name="room"),
    #url(r'^app/(?P<app_slug>[-\w]+)/settings/$', settings, name="app"),
    
)
