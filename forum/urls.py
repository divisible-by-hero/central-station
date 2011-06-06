from django.conf.urls.defaults import *


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', homepage),


    url(r'^admin/', include(admin.site.urls)),

)


