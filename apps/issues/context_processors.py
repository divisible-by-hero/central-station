from issues.choices import *

def constants(request):
    context = {}
    context['issue_priorities'] = ISSUE_PRIORITIES
    context['issue_types'] = ISSUE_TYPES
    context['status_choices'] = STATUS_CHOICES
    return context
    
    
