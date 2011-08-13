from django.conf.urls.defaults import patterns, include, url
from forum.views import view_forum_app

urlpatterns = patterns('',
    
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
    url(r'^app/(?P<app_slug>[-\w]+)/forum/$', view_forum_app, name="view_forum_app"),
)
