from django.conf.urls.defaults import patterns, include, url
from defects.views import *

urlpatterns = patterns('',
    url(r'^$', defect_list, name="defect_list"),
    url(r'^view/(?P<defect_id>\d+)/$', defect_detail, name="defect_detail"),
    url(r'^add/$', add_defect, name="add_defect"),
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
#    url(r'^api/', include('bookmarks.api.urls')),
#    
)
