from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'newsfeed.views.dashboard'),
    url(r'^defects/', include('defects.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^browser/', include('browser.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media'}),
)