__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django.conf.urls import patterns, url

from projects.views import AddProject

urlpatterns = patterns('',

    #url(r'^(?P<goal_slug>[-\w]+)')

    url(r'^add/$', AddProject.as_view(), name='project_add'),
)
