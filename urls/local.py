from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'newsfeed.views.dashboard'),
    url(r'^issues/', include('issues.urls')),
    url(r'^settings/$', 'core.views.change_settings'),
    url(r'^docs/', include('api_docs.urls')),
   
    url(r'^projects/', include('projects.urls')),
    
    url(r'^users/', include('profile.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'profile/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'profile/logout.html'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += staticfiles_urlpatterns()