from django.conf.urls.defaults import patterns, include, url
# Import your views and feeds from your app.

from browser.views import *

urlpatterns = patterns('',
    
    url(r'^repos/$', repos, name="repos"),
    url(r'^browser/$', view_repo, name="view_repo"),
    url(r'^view/(?P<file_name>[-\w./]+)/$', view_file, name="view_file"),
    url(r'^view_dir/(?P<app_slug>[-\w]+)/(?P<path>[-\w./]+)', view_dir),
    url(r'^switch_branch/(?P<branch>[-\w]+)/$', switch_branch),
    url(r'^app/(?P<app_slug>[-\w]+)/repo' , view_app_repo, name="view_app_repo"),
)
