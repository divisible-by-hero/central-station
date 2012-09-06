__author__ = 'Derek Stegelman'
__date__ = '9/6/12'
from tastypie.resources import ModelResource
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import ReadOnlyAuthorization

from sprints.models import Sprint

class SprintResource(ModelResource):

    class Meta:
        queryset = Sprint.objects.all()
        resource = "sprint"
        allowed_methods = ['get']


