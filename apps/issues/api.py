from tastypie.resources import ModelResource
from issues.models import Issue

class IssueResource(ModelResource):
    class Meta:
        queryset = Issue.objects.all()
        resource = 'issues'
        allowed_methods = ['get']

