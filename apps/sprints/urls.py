__author__ = 'Derek Stegelman'
__date__ = '9/5/12'


from django.conf.urls import patterns, url, include

from tastypie.api import Api

from sprints.api import SprintResource
from sprints.views import SprintListView, SprintDetailView

v1_api = Api(api_name="v1")
v1_api.register(SprintResource())

urlpatterns = patterns('',

    url(r'^$', SprintListView.as_view(), name='sprint_list_view'),
    url(r'^?P(<pk>)/$', SprintDetailView.as_view()),

    # API
    url(r'^api/', include(v1_api.urls)),
)
