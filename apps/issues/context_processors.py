from issues.choices import *
from issues.models import *

def constants(request):
    context = {}
    context['issue_priorities'] = ISSUE_PRIORITIES
    context['issue_types'] = ISSUE_TYPES
    context['status_choices'] = STATUS_CHOICES
    return context
    
    
def project_milestones(request, *args, **kwargs):
    context = {}
    try:
        if kwargs.pop('app_slug'):
            context['project_milestones'] = Milestone.objects.filter(app__slug=app_slug)
    except:
        pass
    return context