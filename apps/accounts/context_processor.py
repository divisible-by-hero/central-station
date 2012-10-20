__author__ = 'Derek Stegelman'
__date__ = '10/19/12'

from accounts.models import RoleAssigned, Account
from sprints.models import Sprint
from sprints.forms import SprintForm

def accounts(request):
    try:
        teams = RoleAssigned.objects.filter(user=request.user)
        account = Account.objects.get(slug=request.session.get('account_slug'))
        context = {'teams': teams, 'account_slug': request.session.get('account_slug')}
        account_sprints = Sprint.objects.current().filter(team__organization__slug=request.session.get('account_slug'))
        context['account_sprints'] = account_sprints
        context['account'] = account
        context['sprint_form'] = SprintForm
    except:
        context = {}
        pass

    return context