from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', 'django_cas.views.login', name="login"),
    url(r'^accounts/logout/$', 'django_cas.views.logout', name="logout"),
    url(r'^admin/logout/$', 'django_cas.views.logout'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': './media'}),
)