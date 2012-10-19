__author__ = 'Derek Stegelman'
__date__ = '10/19/12'

from accounts.models import RoleAssigned
from sprints.models import Sprint

def accounts(request):
    teams = RoleAssigned.objects.filter(user=request.user)
    context = {'teams': teams, 'account_slug': request.session.get('account_slug')}
    account_sprints = Sprint.objects.current().filter(team__organization__slug=request.session.get('account_slug'))
    context['account_sprints'] = account_sprints
    return context