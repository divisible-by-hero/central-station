from django.conf.urls.defaults import *
from defects.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', homepage, name="homepage"),
    url(r'^projects/(?P<project_slug>[-\w]+)/$', defect_list, name="defect_list"),
    url(r'^defect/(?P<defect_id>\d+)/$', defect_detail, name="defect_detail"),

    #url(r'^admin/', include(admin.site.urls)),

)


