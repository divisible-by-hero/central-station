from django.conf.urls.defaults import patterns, include, url
# Import your views and feeds from your app.
from blog.views import *
from blog.feeds import BlogFeed

urlpatterns = patterns('',
    
    # Homepage url , always name your URLS
    url(r'^$', homepage, name="homepage"),
    # URl with add and nothing after
    url(r'^add/$', add, name="add_post"),
    # Feed URL
    url(r'^feed/$', BlogFeed()),
    # This is the pattern for ids or other integers
    #url(r'^edit/(?P<bookmark_id>\d+)/$', edit_bookmark, name="edit_bookmark"),
    # This is the pattern for a slug, or alpha chars.
    url(r'^post/(?P<post_slug>[-\w]+)/$', post, name="post"),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', tag, name="tag"),
    url(r'^category/(?P<category_slug>[-\w]+)/$', category, name="category"),
    # Redirect to API urls.
    url(r'^api/', include('blog.api.urls')),
    
)
