from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

__author__ = 'Derek Stegelman'
__date__ = '9/5/12'

admin.autodiscover()

from sprints.ajax import update_status, change_task

urlpatterns = patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/login.html'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'core.views.homepage', name='homepage'),
    url(r'^myprofile/$', 'accounts.views.profile', name='user_profile'),
    url(r'^registration/$', 'accounts.views.registration', name="account_registration"),


    url(r'^ajax/sprints/', include('sprints.ajax_urls')),



    url(r'^projects/', include('projects.urls')),
    url(r'^activity/', include('actstream.urls')),
    url(r'^(?P<account>[-\w]+)/', include('accounts.urls')),
    url(r'^(?P<account>[-\w]+)/sprints/', include('sprints.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'accounts/login.html'}, name="logout"),


    #AJAX
    url(r'^ajax/update/task/(?P<task_id>\d+)/$', change_task, name='ajax_change_task'),
    url(r'^ajax/update/story/(?P<story_id>\d+)/$', update_status, name='ajax_update_status'),


)

if settings.DEBUG:

    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

    urlpatterns += staticfiles_urlpatterns()