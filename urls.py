from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.homepage', name='homepage'),
    url(r'^myprofile/$', 'accounts.views.profile', name='user_profile'),
    url(r'^(?P<account>[-\w]+)/', include('accounts.urls')),
    url(r'^(?P<account>[-\w]+)/sprints/', include('sprints.urls')),

    url(r'^projects/', include('projects.urls')),
    url(r'^activity/', include('actstream.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/login.html'}, name="logout"),


)

if settings.DEBUG:

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

    urlpatterns += staticfiles_urlpatterns()