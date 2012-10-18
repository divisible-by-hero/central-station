__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'core.views.homepage', name='homepage'),
    url(r'^(?P<account>[-\w]+)/sprints/', include('sprints.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/login.html'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

    urlpatterns += staticfiles_urlpatterns()