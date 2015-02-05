__author__ = 'Derek Stegelman'
__date__ = '9/6/12'
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization

from sprints.models import Sprint, Roadblock, Story

class SprintResource(ModelResource):

    class Meta:
        queryset = Sprint.objects.all()
        resource = "sprint"
        allowed_methods = ['get']


class StoryResource(ModelResource):

    class Meta:
        queryset = Story.objects.all()
        resource = "story"
        allowed_methods = ['get']


class RoadBlockResource(ModelResource):

    class Meta:
        queryset = Roadblock.objects.all()
        resource = "roadblock"
        allowed_methods = ['get']