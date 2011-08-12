from django.conf.urls.defaults import patterns, include, url
## Import your views and feeds from your app.
from projects.views import *
#from newapp.feeds import *
#
urlpatterns = patterns('',
    url(r'^apps/$', app_list, name="app_list"),
    url(r'^versions/$', version_list, name="version_list"),
    url(r'^newapp/$' , add_application, name="add_application"),
    url(r'^version/add/$', add_version, name="add_version"),
    url(r'^app/(?P<app_slug>[-\w]+)/$', app, name="app"),
#    # Homepage url , always name your URLS
#    url(r'^$', homepage, name="homepage"),
#    # URl with add and nothing after
#    url(r'^add/$', add, name="add_bookmark"),
#    # Feed URL
#    url(r'^feed/$', BrewFeed()),
#    # This is the pattern for ids or other integers
#    url(r'^edit/(?P<bookmark_id>\d+)/$', edit_bookmark, name="edit_bookmark"),
#    # This is the pattern for a slug, or alpha chars.
#    url(r'^slug/(?P<brew_slug>[-\w]+)/$', delete_bookmark, name="delete_bookmark"),
#    # Redirect to API urls.
    url(r'^api/', include('projects.api.urls')),
#    
)
